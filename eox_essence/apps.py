"""
App configuration for eox_essence.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class EoxEssenceConfig(AppConfig):
    """
    eox-essence configuration.
    """
    name = 'eox_essence'
    verbose_name = 'eox-essence'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'eox-essence',
                'regex': r'^eox-essence/',
                'relative_path': 'urls',
            },
            'cms.djangoapp': {
                'namespace': 'eox-essence',
                'regex': r'^eox-essence/',
                'relative_path': 'urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'production': {'relative_path': 'settings.production'},
            },
            'cms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'production': {'relative_path': 'settings.production'},
            },
        }
    }
