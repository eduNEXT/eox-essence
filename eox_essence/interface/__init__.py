"""
"""
import logging
from importlib import import_module

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)


class EoxEssenceAPIBase():
    """"""

    def __init__(self, interface):
        self.setting_name = 'EOX_ESSENCE_{}'.format(interface.upper())
        self.backend_settings = getattr(settings, self.setting_name, {})

    def get_model(self, **kwargs):
        """
        """
        module_settings = self.backend_settings.get('model', {})

        module = self.get_module(module_settings)
        method = self.get_method(module_settings, 'get')
        valid_parameters = self.get_valid_parameters(module_settings, **kwargs)

        try:
            return self.execute_method(module, method, **valid_parameters)
        except Exception:
            pass

        try:
            return module.objects.get(**valid_parameters)
        except ObjectDoesNotExist:
            return None

    def get_serialized(self, **kwargs):
        """
        """
        module_settings = self.backend_settings.get('serialized', {})

        module = self.get_module(module_settings)
        method = self.get_method(module_settings, 'get')
        valid_parameters = self.get_valid_parameters(module_settings, **kwargs)

        return self.execute_method(
            module,
            method,
            **valid_parameters
        )

    def get_backend(self, backend_route):
        """
        """
        try:
            return import_module(backend_route)
        except ImportError:
            logger.error(
                'Invalid setting value [%s] for %s',
                backend_route,
                self.setting_name,
            )
            raise Exception('custom exception')

    def get_module(self, module_settings):

        backend = self.get_backend(module_settings.get('backend'))
        try:
            return getattr(backend, module_settings.get('name'))
        except AttributeError:
            raise Exception('another custom')

    def get_method(self, module_settings, method_name):

        return module_settings.get(method_name, '')

    def get_valid_parameters(self, module_settings, **kwargs):
        """
        """
        return {
            key: value
            for (key, value) in kwargs.items()
            if key in module_settings.get('allowed_parameters', [])
        }

    def execute_method(self, module, method, **kwargs):
        """
        """

        try:
            func = getattr(module, method)
            return func(**kwargs)
        except AttributeError:
            logger.error(
                'Invalid get_method value [%s] for %s',
                method,
                self.setting_name,
            )
            raise Exception('another custom exception')
