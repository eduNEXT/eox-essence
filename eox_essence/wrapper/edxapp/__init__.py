# -*- coding: utf-8 -*-
"""This module contains all the wrappers for https://github.com/edx/edx-platform.

This contains multiples modules which are analogous to an edx-platform django app, the
structure in this folder is the following:

    ├── edxapp
        ├── __init__.py
        ├── wrapped-django-app-1.py
        ├── wrapped-django-app-2.py
        │
        ├── wrapped-django-app-n.py
        ├── tests
            ├── test-django-app-1.py
            │
            ├── test-django-app-n.py


wrapped-django-app: A analogous module to a edx-platform django application.

    Example:
        courseware -->https://github.com/edx/edx-platform/tree/master/lms/djangoapps/courseware

    This file doesn't wrap all the original modules inside the application, just the necessary or the
    valid contributions.

    Example file:

    from eox_essence.wrapper.edxapp import get_module

    module_1 = get_module(django_app_name, module_name_1)
    module_2 = get_module(django_app_name, module_name_2)

    module_n = get_module(django_app_name, module_name_n)

Modules:
    enrollments: Abstract backend for enrollments djangoapp.
    student: Abstract backend for student djangoapp.

Methods:
    get_module: Return module securely.
"""
import logging
from importlib import import_module

from django.conf import settings

logger = logging.getLogger(__name__)


def get_module(app_name, module):
    """
    Return module securely.
    """
    setting_name = 'EOX_ESSENCE_{}'.format(app_name.upper())
    backend_settings = getattr(settings, setting_name)
    alternative_backends = backend_settings.get('alternative_backends', {})

    if module in alternative_backends:
        return import_module(alternative_backends[module])

    backend_route = backend_settings.get('default', '')

    try:
        backend = import_module(backend_route)
    except ImportError:
        logger.error(
            'Invalid setting value [%s] for %s',
            backend_route,
            setting_name,
        )
        backend = import_module('eox_essence.wrapper.mimic.{}'.format(app_name))

    return getattr(backend, module)
