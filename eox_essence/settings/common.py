"""
Common Django settings for eox_essence project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from __future__ import unicode_literals

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret-key'


# Application definition

INSTALLED_APPS = []

ROOT_URLCONF = 'eox_essence.urls'


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_TZ = True

EOX_ESSENCE_ENROLLMENTS = {
    'model': {
        'backend': 'student.models',
        'name': 'CourseEnrollment',
        'get': 'get_enrollment',
        'allowed_parameters': [
            'course_key',
            'user',
            'course_id',
        ],
    },
    'serialized': {
        'backend': 'openedx.core.djangoapps.enrollments',
        'name': 'api',
        'get': 'get_enrollment',
        'allowed_parameters': [
            'username',
            'course_id',
        ],
    },

}


def plugin_settings(settings):
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """
    settings.EOX_ESSENCE_ENROLLMENTS = EOX_ESSENCE_ENROLLMENTS
