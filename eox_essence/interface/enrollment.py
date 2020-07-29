"""
"""
from django.conf import settings
from django.contrib.auth.models import User
from opaque_keys import InvalidKeyError
from opaque_keys.edx.keys import CourseKey

from eox_essence.interface import EoxEssenceAPIBase


class EnrollmentEoxEssenceAPI(EoxEssenceAPIBase):
    """"""

    setting_name = 'EOX_ESSENCE_ENROLLMENTS'
    backend_settings = getattr(settings, 'EOX_ESSENCE_ENROLLMENTS', {})

    @classmethod
    def get_model(cls, username, course_id, **kwargs):
        """
        """
        try:
            kwargs.update({
                'course_id': course_id,
                'course_key': CourseKey.from_string(course_id),
                'user': User.objects.get(username=username),
            })

            return super().get_model(**kwargs)
        except InvalidKeyError as error:
            # TO-DO Custom exception
            Exception(error)

    @classmethod
    def get_serialized(cls, username, course_id, **kwargs):
        """
        """
        try:
            kwargs.update({
                'username': username,
                'course_id': course_id,
            })

            return super().get_serialized(**kwargs)
        except InvalidKeyError as error:
            # TO-DO Custom exception
            Exception(error)
