from calculator import Calculator
from datastructures import WeatherData


class Parser:

    def __init__(self):
        self.calculation_instance = Calculator()
        self.day_data=[]

    def parse_file_data(self,file_data):
        file_name = [file_data[1]]
        for line in file_data[2:]:
            values = line.replace('\n', '').split(',')[1:]
            self.day_data = []
            self.day_data.append(line.split(',')[0])
            for value in values:
                self.parse_value(value)

            self.calculation_instance.weather_data.append(WeatherData(file_name, self.day_data))

    def parse_value(self,value):
        if value.replace('-', '').isdigit():
            self.day_data.append(int(value))
        elif value.replace('.', '', 1).replace('-', '').isdigit():
            self.day_data.append(float(value))
        else:
            self.day_data.append(value)

    def parser(self,files_data):

        for file_data in files_data:
            self.parse_file_data(file_data)

        return self.calculation_instance
