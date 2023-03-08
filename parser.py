from calculator import Calculator
from data_structures import WeatherData
import utils
from datetime import datetime


class Parser:
    
    @classmethod
    def parse_file_data(cls, file_data, file_name,weather_data):
        for line in file_data[2:]:
            values = line.replace('\n', '').split(',')[1:]
            day_data = [datetime.strptime(line.split(',')[0], '%Y-%m-%d')]
            for value in values:
                cls.parse_value(value, day_data)

            weather_data.append(WeatherData(file_name, day_data))
            
    @staticmethod
    def parse_value(value,day_data):
        if utils.is_digit(value):
            day_data.append(int(value))
        elif utils.is_float(value):
            day_data.append(float(value))
        else:
            day_data.append(value)
            
    @classmethod
    def parser(cls, files_data, files_name):
        weather_data: list[WeatherData] = []
        for file_data, file_name in zip(files_data, files_name):
            cls.parse_file_data(file_data, file_name, weather_data)

        return weather_data
