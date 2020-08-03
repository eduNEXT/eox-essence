"""
"""
from django.conf import settings

from eox_essence.interface import AbstractEoxEssenceAPI


class EnrollmentEoxEssenceAPI(AbstractEoxEssenceAPI):
    """"""

    api_settings = {
        'model_api': {
            'backend': settings.EOX_ESSENCE_ENROLLMENTS.get('model_api'),
            'name': 'EnrollmentsModelWrapper',
        },
        'serialized_api': {
            'backend': settings.EOX_ESSENCE_ENROLLMENTS.get('serialized_api'),
            'name': 'EnrollmentsSerializedWrapper',
        },
    }

    @classmethod
    def get_model_settings(cls):
        """
        """
        return cls.api_settings['model_api']

    @classmethod
    def get_serialized_settings(cls):
        """
        """
        return cls.api_settings['serialized_api']
