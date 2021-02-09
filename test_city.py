import unittest
from city import fmtCity


class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        answer = fmtCity('beijing', 'china')
        self.assertEqual(answer, 'Beijing China')


unittest.main()
