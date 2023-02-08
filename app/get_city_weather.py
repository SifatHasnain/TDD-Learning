import requests
from configparser import ConfigParser
import os
from dateutil import parser

config_file_path = 'config.ini'

class CityTemperature:
    def __init__(self, start_date: str, end_date: str, city_name: str) -> None:

        # TODO: Mock these values in the test file
        self.start_date = start_date
        self.end_date = end_date
        self.city_name = city_name

        # TODO: Add config manager
        # self.config_parser = ConfigParser()
        # TODO: Read from config file
        self.city_list = ["dhaka", "paris", "new york", "sydney", "singapore"]

    def get_temperature(self) -> list:
        NotImplementedError