"""
"""
from django.contrib.auth.models import User
from opaque_keys import InvalidKeyError
from opaque_keys.edx.keys import CourseKey

from eox_essence.wrapper.edxapp.enrollments import api
from eox_essence.wrapper.edxapp.student import models


def get_enrollment(username, course_id, serialized=False):
    """
    """
    try:
        if not serialized:
            course_key = CourseKey.from_string(course_id)
            user = User.objects.get(username=username)

            return models.CourseEnrollment.get_enrollment(
                user=user,
                course_key=course_key,
            )

        return api.get_enrollment(username, course_id)

    except InvalidKeyError as error:
        # TO-DO Custom exception
        Exception(error)


def get_enrollment_model(username, course_id):
    """
    """
    try:
        course_key = CourseKey.from_string(course_id)
        user = User.objects.get(username=username)

        return models.CourseEnrollment.get_enrollment(
            user=user,
            course_key=course_key,
        )

    except InvalidKeyError as error:
        # TO-DO Custom exception
        Exception(error)


def get_serialized_enrollment(username, course_id):
    """
    """
    try:
        return api.get_enrollment(username, course_id)
    except InvalidKeyError as error:
        # TO-DO Custom exception
        Exception(error)
