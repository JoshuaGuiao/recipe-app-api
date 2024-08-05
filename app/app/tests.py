"""
Sample Test
"""

from django.test import SimpleTestCase  # type: ignore

from app import calc


class CalcTest(SimpleTestCase):
    """ Test the calc method"""

    def test_add_number(self):
        """ adding number together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_number(self):
        """ subtracting number together"""
        res = calc.subtract(6, 5)
        self.assertEqual(res, 1)
