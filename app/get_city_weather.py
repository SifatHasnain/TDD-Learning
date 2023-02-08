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
        date_format = '%d/%m/%Y'
        
        # TODO: check is not proper
        try:
            start_date = parser.parse(self.start_date).date()
            end_date = parser.parse(self.end_date).date()
        except:
            raise ValueError
        finally:
            print('Required Date Format: DD/MM/YYY')

        if self.city_name.lower() not in self.city_list or (end_date<start_date):
            print('Check Input: City is not supported or Time Range is invalid')
            raise ValueError 
        
        # TODO: Add Config Manager to rad API_KEY, BASE_URL and SUPPORT_CITY
        # config = self.config_parser.read_file(config_file_path)

        API_KEY="" #read from config file after creating account for API access
        BASE_URL="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" # read from config file
        
        URL = f"{BASE_URL}/{self.city_name}/{start_date}/{end_date}?key={API_KEY}&include=days&elements=temp" # replace by config params
        
        request = requests.get(URL)

        response = {}
        response['status_code'] = request.status_code
        if request.status_code == 200:
            temperature_list = [data['temp'] for data in request.json()['days']]
            response['data'] = temperature_list

            return response
        
        return None