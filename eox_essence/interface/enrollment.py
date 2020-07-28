"""
"""
from django.contrib.auth.models import User
from opaque_keys import InvalidKeyError
from opaque_keys.edx.keys import CourseKey

from eox_essence.interface import EoxEssenceAPIBase


class EnrollmentEoxEssenceAPI(EoxEssenceAPIBase):
    """"""

    def __init__(self):
        super().__init__('enrollments')

    def get_model(self, username, course_id):
        """
        """
        try:
            parameters = {
                'user': User.objects.get(username=username),
                'course_key': CourseKey.from_string(course_id),
            }

            return super().get_model(**parameters)

        except InvalidKeyError as error:
            # TO-DO Custom exception
            Exception(error)

    def get_serialized(self, username, course_id):
        """
        """
        try:
            parameters = {
                'username': username,
                'course_id': course_id,
            }
            return super().get_serialized(**parameters)
        except InvalidKeyError as error:
            # TO-DO Custom exception
            Exception(error)
