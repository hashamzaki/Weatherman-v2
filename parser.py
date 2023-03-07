from calculator import Calculator
from datastructures import WeatherData


class Parser:
    @classmethod
    def parser(self,files_data):

        calculation_instance = Calculator()
        for file_data in files_data:
            file_name = [file_data[1]]
            for line in file_data[2:]:
                values = line.replace('\n', '').split(',')[1:]
                day_data = [line.split(',')[0]]
                for value in values:
                    if value.replace('-', '').isdigit():
                        day_data.append(int(value))
                    elif value.replace('.', '', 1).replace('-', '').isdigit():
                        day_data.append(float(value))
                    else:
                        day_data.append(value)

                calculation_instance.weather_data.append(WeatherData(file_name, day_data))

        return calculation_instance