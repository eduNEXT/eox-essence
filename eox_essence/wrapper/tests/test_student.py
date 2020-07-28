"""Tests file for student wrapper.

Classes:
    WrapperStudentTestCase: Test right initialization.
"""
from importlib import reload

from django.conf import settings
from django.test import TestCase
from mock import patch

from eox_essence.wrapper.edxapp import student


class WrapperStudentTestCase(TestCase):
    """Test the three cases defined in the init file."""

    @patch('eox_essence.wrapper.edxapp.get_module')
    def test_initialize_right_values(self, get_module_mock):
        """
        This method tests that the module is initialized with the right
        values for student.

        Expected behavior:
            - import_module is called once with the right setting value.
        """
        reload(student)

        get_module_mock.assert_called_with('student', 'models')

    def test_setting_value(self):
        """
        This method tests that the module is initialized with the right
        values for student.

        Expected behavior:
            - Return the expected result.
        """
        self.assertEqual('student', settings.EOX_ESSENCE_STUDENT['default'])

    def test_has_right_attributes(self):
        """
        This method tests that the mimic file has the right right attributes.

        Expected behavior:
            - The module has all the attributes.
        """
        expected_attributes = [
            'models',
        ]

        attributes = [hasattr(student, attribute) for attribute in expected_attributes]

        self.assertTrue(all(attributes))
