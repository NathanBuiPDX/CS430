import requests
from datetime import datetime, timedelta, timezone
import os

DEFAULT_CITY = "Portland"
FAHRENHEIT_UNIT = 'imperial'
CELSIUS_UNIT = 'metric'
API_KEY = os.getenv('API_KEY')

def get_local_city_time(offset):
    """
    Gets the timezone offset from the city and format the offset to display the city's current local time
    :return: dict contains formatted local date and time of the city
    """
    try:
        print("offset: ", offset)
        now = datetime.now(timezone.utc)
        utc_offset = now.astimezone().utcoffset().total_seconds() // 60  # Convert seconds to minutes
        city_offset = offset
        local_time = now + timedelta(seconds=(utc_offset + city_offset) * 60)  # Convert minutes to seconds
        datetime_object = {}
        datetime_object['date'] = local_time.strftime('%A, %b %d, %Y')
        datetime_object['time'] = local_time.strftime('%I:%M %p')
        return datetime_object
    except Exception as err:
        print(err)
        print(f"Unable to get current time for the city")
        
def getWeatherData(city, tempUnit):
    """
    Gets the city and the temperature unit to make a GET request to openweathermap API
    :return: dict contains city's data
    """
    data = {}
    try:
        resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={tempUnit}')
        data = resp.json()
        if tempUnit == CELSIUS_UNIT:
            data['tempUnit'] = 'C'
        elif tempUnit == FAHRENHEIT_UNIT:
            data['tempUnit'] = 'F'
        data['dateTime'] = get_local_city_time(data['timezone'])

        print("final data in from GET call: ", data)
    except requests.exceptions.HTTPError as e:
        print (e.response.text)
    return data

def formatForecastData(list, unit):
    """
    Gets a list of the city 3-hour time invertals forecast and the temperature unit.
    :return: dict contains time, max/min temperature, main weather, and temperature unit of the city
    """
    formattedData = []
    tempUnit = 'C' if unit == CELSIUS_UNIT else 'F'
    for data in list:
        temp = {}
        temp['time'] = datetime.utcfromtimestamp(data['dt']).strftime('%I %p')
        temp['tempMax'] = data['main']['temp_max']
        temp['tempMin'] = data['main']['temp_min']
        temp['weather'] = data['weather'][0]['main']
        temp['tempUnit'] = tempUnit
        formattedData.append(temp)
        
    print("formattedData: ", formattedData)
    return formattedData

def getForecastData(city, tempUnit):
    """
    Gets the city and the temperature unit to make a GET request to openweathermap API.
    :return: a list contains data of 3-hour time intervals of the city
    """
    data = {}
    try:
        resp = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={tempUnit}&cnt=8')
        data = resp.json()
        print("forecast data: ", data)
        data['forecastData'] = formatForecastData(data['list'], tempUnit)
    except requests.exceptions.HTTPError as e:
        print (e.response.text)
    return data
        
class model():
    def __init__(self):
        # Make sure our database exists
        self.data = {}
        self.city = DEFAULT_CITY
        self.tempUnit = FAHRENHEIT_UNIT
        self.data = getWeatherData(DEFAULT_CITY, FAHRENHEIT_UNIT)
        
    def cityData(self):
        """
        :return: a dict contains city's data
        """
        return self.data
    
    def fetchCityData(self, city):
        """
        Gets the city's name
        :return: a dict contains city's data
        """
        self.city = city
        self.data = getWeatherData(city, self.tempUnit)
        return self.data
        
    def fetchNewTempUnitData(self, tempUnit):
        """
        Gets the temperature unit
        :return: a dict contains city's data with updated temperature unit
        """
        self.tempUnit = tempUnit
        self.data = getWeatherData(self.city, tempUnit)
        return self.data
    
    def fetchForecastData(self):
        """
        :return: a dict contains city's data 3-hour time intevals for the next 24 hours
        """
        data = getForecastData(self.city, self.tempUnit)
        data['city'] = self.city
        data['dateTime'] = self.data['dateTime']
        return data