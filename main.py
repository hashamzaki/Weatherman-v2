import sys
from os import listdir
from os.path import join , isfile
import calendar


class Weather:
    def __init__(self, filename, day_data):
        self.filename = filename
        self.day_data = day_data


class Calculations:
    def __init__(self):
        self.weather_data=[]

    def find_highest_in_year(self):
        max_temp = -999
        day = ""
        month = ""

        for data in self.weather_data:

            if(data.day_data[0].split('-')[0] == sys.argv[2]) and data.day_data[1] != "":

                if data.day_data[1] > max_temp:
                    max_temp=data.day_data[1]
                    month = data.day_data[0].split('-')[1]
                    day = data.day_data[0].split('-')[2]

        print(f"Highest: {max_temp}C on {calendar.month_abbr[int(month)]} {day} ")

    def find_lowest_in_year(self):
        min_temp = 999
        day = ""
        month = ""

        for data in self.weather_data:

            if (data.day_data[0].split('-')[0] == sys.argv[2]) and data.day_data[3] != "":

                if data.day_data[3] < min_temp:
                    min_temp = data.day_data[3]
                    month = data.day_data[0].split('-')[1]
                    day = data.day_data[0].split('-')[2]

        print(f"Lowest: {min_temp}C on {calendar.month_abbr[int(month)]} {day} ")

    def find_most_humid_in_year(self):
        max_temp = -999
        day = ""
        month = ""

        for data in self.weather_data:

            if(data.day_data[0].split('-')[0] == sys.argv[2]) and data.day_data[8] != "":

                if data.day_data[8] > max_temp:
                    max_temp = data.day_data[8]
                    month = data.day_data[0].split('-')[1]
                    day = data.day_data[0].split('-')[2]

        print(f"Humidity: {max_temp}% on {calendar.month_abbr[int(month)]} {day} ")


def read_one_file(file_path):

    with open(file_path, mode='r') as reader:
        file_data_line = reader.readlines()
    file_data_line.insert(1, file_path)

    return file_data_line


def read_all_file(file_path):

    files_name_list = listdir(file_path)
    files_data = []
    for file_name in files_name_list:
        files_data.append(read_one_file(join(file_path, file_name)))

    return files_data


def parser(files_data):

    calculation_instance = Calculations()
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

            calculation_instance.weather_data.append(Weather(file_name, day_data))

    return calculation_instance


if __name__ == '__main__':

    if sys.argv[1] == '-e':
        files_data = read_all_file('/home/faran/Downloads/weatherfiles (1)/weatherfiles')
        calculation_instance = parser(files_data)
        calculation_instance.find_highest_in_year()
        calculation_instance.find_lowest_in_year()
        calculation_instance.find_most_humid_in_year()


