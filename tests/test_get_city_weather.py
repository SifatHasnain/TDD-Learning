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

    def test_get_temperature__when_given_incorrect_city__should_raise_ValueError(self):
        self.service: CityTemperature = CityTemperature(self.start_date, self.end_date, 'Delhi')
        
        with self.assertRaises(ValueError):
            self.service.get_temperature()
    
    
    def test_get_temperature__when_given_incorrect_time_range__should_raise_ValueError(self):
        self.service: CityTemperature = CityTemperature('30/01/2023', '20/01/2023', self.city_name)
        
        with self.assertRaises(ValueError):
            self.service.get_temperature()

    def test_get_temperature__when_given_incorrect_date_format__should_raise_ValueError(self):
        self.service: CityTemperature = CityTemperature('2023-01-20', '2023-01-23', self.city_name)
        
        with self.assertRaises(ValueError):
            self.service.get_temperature()

    @patch('app.get_city_weather.requests.get')
    def test_get_temperature__when_given_correct_input__should_return_list_of_daily_temperatures(self, mocked_requests):

        self.service: CityTemperature = CityTemperature(self.start_date, self.end_date, self.city_name)
        mocked_requests.return_value.status_code = 200
        
        self.assertEqual(self.service.get_temperature()['status_code'], 200)
