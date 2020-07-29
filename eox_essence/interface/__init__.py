"""
"""
import logging
from importlib import import_module

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model

from eox_essence.interface.exceptions import (
    EoxEssenceBadConfiguration,
    EoxEssenceInvalidBackend,
    EoxEssenceInvalidMethod,
    EoxEssenceInvalidModule,
    EoxEssenceInvalidParameters,
)

logger = logging.getLogger(__name__)


class EoxEssenceAPIBase():
    """"""

    def __init__(self, interface):
        self.setting_name = 'EOX_ESSENCE_{}'.format(interface.upper())
        self.backend_settings = getattr(settings, self.setting_name, {})

    def get_model(self, **kwargs):
        """
        """
        try:
            return self.execute_method(
                module_name='model',
                method_name='get',
                **kwargs
            )
        except EoxEssenceInvalidMethod:
            pass

        module_settings = self.backend_settings.get('model')
        module = self.get_module(module_settings)

        if not issubclass(module, Model):
            message = 'The module[{}] is not a subclass of django models.'.format(
                module.__name__,
            )
            raise EoxEssenceInvalidModule(message)

        valid_parameters = self.filter_parameters(
            module_settings.get('allowed_parameters', []),
            **kwargs
        )

        try:
            return module.objects.get(**valid_parameters)
        except ObjectDoesNotExist:
            return None

    def get_serialized(self, **kwargs):
        """
        """
        return self.execute_method(
            module_name='serialized',
            method_name='get',
            **kwargs
        )

    def get_backend(self, backend_route):
        """
        """
        if not backend_route:
            message = 'Backend route can not be empty.'
            raise EoxEssenceInvalidBackend(message)

        try:
            return import_module(backend_route)
        except ImportError:
            message = 'The backen route[{}] is not valid.'.format(backend_route)
            raise EoxEssenceInvalidBackend(message)

    def get_module(self, module_settings):
        """
        """
        attribute_name = module_settings.get('name')
        backend = self.get_backend(module_settings.get('backend'))

        if not attribute_name or not hasattr(backend, attribute_name):
            message = 'The current backend for the route [{}] has no attribute called [{}].'.format(
                backend.__file__,
                attribute_name,
            )
            raise EoxEssenceInvalidModule(message)

        return getattr(backend, attribute_name)

    def filter_parameters(self, allowed_parameters, **kwargs):
        """
        """
        return {
            key: value
            for key, value in kwargs.items()
            if key in allowed_parameters
        }

    def execute_method(self, module_name, method_name, **kwargs):
        """
        """
        module_settings = self.backend_settings.get(module_name)

        if not module_settings:
            message = 'There is no a valid value for[{}] in {}.'.format(
                module_name,
                self.setting_name,
            )
            raise EoxEssenceBadConfiguration(message)

        method = module_settings.get(method_name)
        module = self.get_module(module_settings)

        if not method or not hasattr(module, method):
            message = 'There is no valid settings for the method [{}].'.format(method_name)
            raise EoxEssenceInvalidMethod(message)

        func = getattr(module, method)

        try:
            return func(
                **self.filter_parameters(
                    module_settings.get('allowed_parameters', []),
                    **kwargs
                )
            )
        except TypeError as error:
            raise EoxEssenceInvalidParameters(error)
