from calculator import Calculator
from data_structures import WeatherData
import utils
from datetime import datetime


class Parser:

    def __init__(self):
        self.weather_data: list[WeatherData] = []
        self.day_data = []

    def parse_file_data(self, file_data, file_name):
        for line in file_data[2:]:
            values = line.replace('\n', '').split(',')[1:]
            self.day_data = []
            self.day_data.append(datetime.strptime(line.split(',')[0], '%Y-%m-%d'))
            for value in values:
                self.parse_value(value)

            self.weather_data.append(WeatherData(file_name, self.day_data))

    def parse_value(self, value):
        if utils.is_digit(value):
            self.day_data.append(int(value))
        elif utils.is_float(value):
            self.day_data.append(float(value))
        else:
            self.day_data.append(value)

    def parser(self, files_data, files_name):

        for file_data, file_name in zip(files_data, files_name):
            self.parse_file_data(file_data, file_name)

        return self.weather_data
