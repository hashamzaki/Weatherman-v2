import calendar
import sys

import datastructures


class Calculator:
    def __init__(self):
        self.weather_data: list[datastructures.WeatherData] = []

    def find_highest_in_year(self):
        max_temperature = float('-inf')
        day = ""
        month = ""

        for data in self.weather_data:

            if (data.day_data[0].split('-')[0] == sys.argv[2]) \
                    and data.day_data[1] != "" and data.day_data[1] > max_temperature:

                max_temperature=data.day_data[1]
                month = data.day_data[0].split('-')[1]
                day = data.day_data[0].split('-')[2]

        print(f"Highest: {max_temperature}C on {calendar.month_abbr[int(month)]} {day} ")

    def find_lowest_in_year(self):
        min_temperature = float('inf')
        day = ""
        month = ""

        for data in self.weather_data:

            if (data.day_data[0].split('-')[0] == sys.argv[2]) \
                    and data.day_data[3] != "" and data.day_data[3] < min_temperature:

                min_temperature = data.day_data[3]
                month = data.day_data[0].split('-')[1]
                day = data.day_data[0].split('-')[2]

        print(f"Lowest: {min_temperature}C on {calendar.month_abbr[int(month)]} {day} ")

    def find_most_humid_in_year(self):
        max_temperature = float('-inf')
        day = ""
        month = ""

        for data in self.weather_data:

            if(data.day_data[0].split('-')[0] == sys.argv[2]) \
                    and data.day_data[8] != "" and data.day_data[8] > max_temperature:

                max_temperature = data.day_data[8]
                month = data.day_data[0].split('-')[1]
                day = data.day_data[0].split('-')[2]

        print(f"Humidity: {max_temperature}% on {calendar.month_abbr[int(month)]} {day} ")
