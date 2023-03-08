import sys
from reader import Reader
from parser import Parser
from calculator import Calculator
from utils import print_most_humid_day, print_highest_temperature, print_lowest_temperature

if __name__ == '__main__':

    if sys.argv[1] == '-e':
        files_data_and_name = Reader.read_all_file('/home/faran/Downloads/weatherfiles (1)/weatherfiles')
        year = int(sys.argv[2])
        calculation_instance = Parser.parser(files_data_and_name['all_files_data'],
                                               files_data_and_name['all_files_names'])
        max_temperature_data = Calculator.find_highest_in_year(calculation_instance, year)
        print_highest_temperature(max_temperature_data['max_temperature'], max_temperature_data['month'],
                                  max_temperature_data['day'])
        min_temperature_data = Calculator.find_lowest_in_year(calculation_instance, year)
        print_lowest_temperature(min_temperature_data['min_temperature'], min_temperature_data['month'],
                                 min_temperature_data['day'])
        max_humidity_data = Calculator.find_most_humid_in_year(calculation_instance, year)
        print_most_humid_day(max_humidity_data['max_humidity'], max_humidity_data['month'],
                             max_humidity_data['day'])
