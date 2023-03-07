from calculator import Calculator
from datastructures import WeatherData


class Parser:

    def parser(self,files_data):
        calculation_instance = Calculator()
        for file_data in files_data:
            self.pars_file_data(file_data)

        return calculation_instance

    def pars_file_data(self, file_data):
        file_name = [file_data[1]]
        for line in file_data[2:]:
            values = line.replace('\n', '').split(',')[1:]
            day_data = [line.split(',')[0]]
            for value in values:
                self.type_cast_value(value)

            self.calculation_instance.weather_data.append(WeatherData(file_name, day_data))

    def type_cast_value(self,value):
        if value.replace('-', '').isdigit():
            self.day_data.append(int(value))
        elif value.replace('.', '', 1).replace('-', '').isdigit():
            self.day_data.append(float(value))
        else:
            self.day_data.append(value)