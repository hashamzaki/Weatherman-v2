from calculator import Calculator
from data_structures import WeatherData
from utils import is_digit,is_float
from datetime import datetime


class Parser:
    
    @classmethod
    def parse_file_data(cls, file_data, file_name):
        weather_data: list[WeatherData] = []
        for line in file_data[1:]:
            values = line.replace('\n', '').split(',')[1:]
            day_data = [datetime.strptime(line.split(',')[0], '%Y-%m-%d')]
            for value in values:
                day_data.append(cls.parse_value(value, day_data))
            weather_data.append(WeatherData(file_name, day_data))

        return weather_data

    @staticmethod
    def parse_value(value, day_data):
        return int(value) if is_digit(value) else float(value) if is_float(value) else value
            
    @classmethod
    def parser(cls, files_data_and_names):
        weather_data: list[WeatherData] = []
        for file_data, file_name in zip(files_data_and_names['all_files_data'], files_data_and_names['all_files_names']):
            weather_data = weather_data + cls.parse_file_data(file_data, file_name)

        return weather_data
