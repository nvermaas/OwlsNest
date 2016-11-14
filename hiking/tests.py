from django.test import TestCase

# Create your tests here.
from .models import Hike

class HikeMethodsTests(TestCase):

    def test_is_year_valid(self):
        """
        Hike.get_year should return a valid year
        """
        print("test_is_year_valid")
        example_date = "oct/nov 2013"
        example_hike = Hike(date=example_date)
        year = Hike.get_year(example_hike)
        ok = year >=1900 and year <=2100
        self.assertIs(ok,True)
