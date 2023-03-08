import calendar
import sys


class Calculator:
    # def __init__(self):
    @staticmethod
    def find_highest_in_year(weather_data, year_to_be_compared):
        max_temperature = float('-inf')
        day = ""
        month = ""
        for data in weather_data:
            data_to_be_compared = data.day_data[1]
            if (data.day_data[0].year == int(year_to_be_compared)) \
                    and data_to_be_compared and data_to_be_compared > max_temperature:

                max_temperature = data_to_be_compared
                month = data.day_data[0].month
                day = data.day_data[0].day
        return {'max_temperature': max_temperature, 'month': month, 'day': day}

    @staticmethod
    def find_lowest_in_year(weather_data, year_to_be_compared):
        min_temperature = float('inf')
        day = ""
        month = ""
        for data in weather_data:
            data_to_be_compared = data.day_data[3]
            if (data.day_data[0].year == int(year_to_be_compared)) \
                    and data_to_be_compared and data_to_be_compared < min_temperature:

                min_temperature = data_to_be_compared
                month = data.day_data[0].month
                day = data.day_data[0].day

        return {'min_temperature': min_temperature, 'month': month, 'day': day}

    @staticmethod
    def find_most_humid_in_year(weather_data, year_to_be_compared):
        max_humidity = float('-inf')
        day = ""
        month = ""
        for data in weather_data:
            data_to_be_compared = data.day_data[8]
            if(data.day_data[0].year == int(year_to_be_compared))  \
                    and data_to_be_compared and data_to_be_compared > max_humidity:

                max_humidity = data_to_be_compared
                month = data.day_data[0].month
                day = data.day_data[0].day

        return {'max_humidity': max_humidity, 'month': month, 'day': day}
