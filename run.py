from app.get_city_weather import CityTemperature

if __name__ == '__main__':
    service = CityTemperature('20/01/2023', '25/01/2023', 'Dhaka')
    data = service.get_temperature()
    if data['status_code'] == 200:
        print("Daily Temperature List", data['data'])
    else:
        print('Something went wrong! Try again!')