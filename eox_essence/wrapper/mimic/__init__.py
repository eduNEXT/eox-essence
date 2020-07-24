# -*- coding: utf-8 -*-
"""This module all the fake data for the supported modules.

This contains multiples modules which contain all the fake attributes, every attribute
should be used only in tests scenarios and there must be one file per each module in the edxapp folder,
every file must contain all attributes required in the edxappp module.

    ├── mimic
        ├── __init__.py
        ├── django-fake-app-1.py
        ├── django-fake-app-2.py
        │
        ├── django-fake-app-n.py


django-fake-app: A file with multiple fake attributes.

    Example file:

    attribute_1 = Mock()
    attribute_2 = object()

    class Attribute_4():

        def fake_method(self):
            return  Mock()

    def attribute_5():
        return Mock()

Modules:
    site_configuration: partial fake module for site_configuration.
"""
