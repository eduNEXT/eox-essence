"""
Production Django settings for eox_essence project.
"""

from __future__ import unicode_literals


def plugin_settings(settings):
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """
    settings.EOX_ESSENCE_ENROLLMENTS = getattr(settings, 'ENV_TOKENS', {}).get(
        'EOX_ESSENCE_ENROLLMENTS',
        settings.EOX_ESSENCE_ENROLLMENTS,
    )
    settings.EOX_ESSENCE_STUDENT = getattr(settings, 'ENV_TOKENS', {}).get(
        'EOX_ESSENCE_STUDENT',
        settings.EOX_ESSENCE_STUDENT,
    )
