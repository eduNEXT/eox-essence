"""
"""
from abc import ABC, abstractmethod

from eox_essence.wrappers import get_module


class AbstractEoxEssenceAPI(ABC):
    """"""

    @classmethod
    @abstractmethod
    def get_model_settings(cls):
        """
        """

    @classmethod
    @abstractmethod
    def get_serialized_settings(cls):
        """
        """

    @classmethod
    def get_model(cls, **kwargs):
        """
        """
        module = get_module(module_settings=cls.get_model_settings())

        return module.get(**kwargs)

    @classmethod
    def get_serialized(cls, **kwargs):
        """
        """
        module = get_module(module_settings=cls.get_serialized_settings())

        return module.get(**kwargs)
