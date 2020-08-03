"""
"""
from eox_essence.wrappers import SerializedWrapperBase, get_module
from eox_essence.wrappers.enrollments import enrollment_settings, serialized_settings


class EnrollmentsSerializedWrapper(SerializedWrapperBase):
    """
    """

    backend_settings = serialized_settings
    model = get_module({
        'backend': enrollment_settings.get('model_api'),
        'name': 'EnrollmentsModelWrapper',
    })

    @classmethod
    def update(cls, **kwargs):
        """
        """
        raise NotImplementedError('Update method is not supported.')

    @classmethod
    def create(cls, **kwargs):
        """
        """
        raise NotImplementedError('Create method is not supported.')
