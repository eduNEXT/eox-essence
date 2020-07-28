"""Tests file for edxapp wrappers.

Classes:
    GetModuleTestCase: Test get_module method.
"""
import logging

from django.conf import settings
from django.test import TestCase
from mock import Mock, patch
from testfixtures import LogCapture

from eox_essence.wrapper.edxapp import get_module
from eox_essence.wrapper.mimic import test_module


class GetModuleTestCase(TestCase):
    """Test all the possibles scenarios for get_module and verifies the right behavior."""

    @patch('eox_essence.wrapper.edxapp.import_module')
    def test_get_alternative_module(self, import_module_mock):
        """
        This method tests the desired behavior when the module is in the
        alternative backend list.

        Expected behavior:
            - Return the expected result.
            - import_module is called once with the right setting value.
        """
        module = Mock()
        module.expected_result = 'This is a test value.'
        import_module_mock.return_value = module

        result = get_module('test_module', 'alternative_module')

        self.assertEqual(module, result)
        import_module_mock.assert_called_once_with(
            settings.EOX_ESSENCE_TEST_MODULE['alternative_backends']['alternative_module']
        )

    @patch('eox_essence.wrapper.edxapp.import_module')
    def test_get_valid_module(self, import_module_mock):
        """
        This method tests the desired behavior when all the parameters
        have been set correctly.

        Expected behavior:
            - Return the expected result.
            - import_module is called once with the right setting value.
        """
        module = Mock()
        module.expected_result = 'This is a test value.'
        import_module_mock.return_value = module

        result = get_module('test_module', 'expected_result')

        self.assertEqual(module.expected_result, result)
        import_module_mock.assert_called_once_with(settings.EOX_ESSENCE_TEST_MODULE['default'])

    def test_get_invalid_module(self):
        """
        This method tests when the module does not exist and the
        mimic module is returned.

        Expected behavior:
            - Log error for the given module.
            - Return the value stored in the mimic test module.
        """
        error_message = 'Invalid setting value [{}] for {}'.format(
            settings.EOX_ESSENCE_TEST_MODULE['default'],
            'EOX_ESSENCE_TEST_MODULE',
        )

        with LogCapture(level=logging.ERROR) as log_capture:
            result = get_module('test_module', 'expected_result')

            log_capture.check(
                (get_module.__module__, 'ERROR', error_message),
            )

        self.assertEqual(test_module.expected_result, result)

    def test_invalid_setting(self):
        """
        This method tests when the module has not been set in the settings file.

        Expected behavior:
            - Raise AttributeError.
        """
        with self.assertRaises(AttributeError):
            get_module('invalid_value', 'expected_result')

    @patch('eox_essence.wrapper.edxapp.import_module')
    def test_invalid_attribute(self, import_module_mock):
        """
        This method tests when the module does not have the required attribute.

        Expected behavior:
            - Raise AttributeError.
            - import_module is called once with the right setting value.
        """
        module = Mock(spec=[])
        import_module_mock.return_value = module

        with self.assertRaises(AttributeError):
            get_module('test_module', 'invalid_attribute')

        import_module_mock.assert_called_once_with(settings.EOX_ESSENCE_TEST_MODULE['default'])
