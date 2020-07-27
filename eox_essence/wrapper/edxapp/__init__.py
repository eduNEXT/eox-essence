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

    from eox_wrapper.edxapp.import_module import get_module

    backend = get_module(django_app_name)

    module_1 = backend.module_1
    module_2 = backend.module_2
    .
    .
    module_n = backend.module_n

Modules:
    import_module: generic import function.
    site_configuration: Abstract backend for site_configuration djangoapp.

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
    backend_route = getattr(settings, setting_name)

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
