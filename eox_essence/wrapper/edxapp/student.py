"""Wrapper file for site_configuration open-edx djangoapp.

This file contains all the wrapped modules for the site_configuration djangoapp.
https://github.com/edx/edx-platform/tree/master/common/djangoapps/student

Attributes:
    models: Open edX Student models.
"""
from eox_essence.wrapper.edxapp import get_module

models = get_module('student', 'models')
