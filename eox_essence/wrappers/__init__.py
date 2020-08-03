from importlib import import_module

from rest_framework.serializers import Serializer

from eox_essence.exceptions import (
    EoxEssenceBadConfiguration,
    EoxEssenceInvalidBackend,
    EoxEssenceInvalidMethod,
    EoxEssenceInvalidModule,
    EoxEssenceInvalidSerializer,
)


def get_backend(backend_route):
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


def get_module(module_settings):
    """
    """
    attribute_name = module_settings.get('name')
    backend = get_backend(module_settings.get('backend'))

    if not attribute_name or not hasattr(backend, attribute_name):
        message = 'The current backend for the route [{}] has no attribute called [{}].'.format(
            backend.__file__,
            attribute_name,
        )
        raise EoxEssenceInvalidModule(message)

    return getattr(backend, attribute_name)


def execute_method(module_settings, method_name, **kwargs):
    """
    """
    if not module_settings:
        raise EoxEssenceBadConfiguration('Missing settings.')

    method = module_settings.get(method_name)
    module = get_module(module_settings)

    if not method or not hasattr(module, method):
        raise EoxEssenceInvalidMethod('Method name is invalid.')

    func = getattr(module, method)

    return func(**kwargs)


class ModelWrapperBase():
    """"""

    backend_settings = {}

    @classmethod
    def get(cls, **kwargs):
        """
        """
        return execute_method(
            module_settings=cls.backend_settings,
            method_name='get',
            **kwargs
        )

    @classmethod
    def update(cls, **kwargs):
        """
        """
        return execute_method(
            module_settings=cls.backend_settings,
            method_name='update',
            **kwargs
        )

    @classmethod
    def create(cls, **kwargs):
        """
        """
        return execute_method(
            module_settings=cls.backend_settings,
            method_name='create',
            **kwargs
        )

    @classmethod
    def delete(cls, **kwargs):
        """
        """
        return execute_method(
            module_settings=cls.backend_settings,
            method_name='create',
            **kwargs
        )


class SerializedWrapperBase():
    """"""

    backend_settings = {}
    model = None

    @classmethod
    def get(cls, **kwargs):
        """
        """
        return cls.serializer(
            instance=cls.model.get(**kwargs),
        ).data

    @classmethod
    def update(cls, **kwargs):
        """
        """
        return cls.serializer(
            instance=cls.model.get(**kwargs),
            data=kwargs,
        ).data

    @classmethod
    def create(cls, **kwargs):
        """
        """
        serializer = cls.serializer(**kwargs)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data()

    @classmethod
    def _serializer(cls):
        serializer = get_module(cls.backend_settings)

        if not issubclass(serializer, Serializer):
            raise EoxEssenceInvalidSerializer('Serializer is not a subclass of rest_framework.serializers.Serializer')

        return serializer

    @classmethod
    def serializer(cls, **kwargs):

        _serializer = cls._serializer()

        return _serializer(**kwargs)
