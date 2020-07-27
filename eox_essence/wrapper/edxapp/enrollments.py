"""Wrapper file for site_configuration open-edx djangoapp.

This file contains all the wrapped modules for the site_configuration djangoapp.
https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/enrollments

Attributes:
    api: Open Edx Enrollment api module.
"""
from eox_essence.wrapper.edxapp import get_module

api = get_module('enrollments', 'api')
