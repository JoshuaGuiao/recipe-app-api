"""
Test custom django mangement commands.
"""
from unittest.mock import patch
# Mock database behaviour to simulate a response

from psycopg2 import OperationalError as Psycopg2Error  # type: ignore
# Possible error to get before the db is ready

from django.core.management import call_command  # type: ignore
# helper function to call a command we are testing
from django.db.utils import OperationalError  # type: ignore
# Possible error to get in db as well
from django.test import SimpleTestCase  # type: ignore
# base test class to use for testing


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test Commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if db is ready"""
        patched_check.return_value = True

        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting Operational Error"""
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
