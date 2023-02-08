import unittest
from unittest import TestCase
from app.get_city_weather import CityTemperature
import datetime
from unittest.mock import Mock, patch

class TestCiyTemperature(TestCase):
    
    def setUp(self):
        self.start_date = '20/01/2023'
        self.end_date = '30/01/2023'
        self.city_name = "Dhaka"

if __name__ == '__main__':
    unittest.main()