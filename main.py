import sys
from inputvalidations import Validator
from os import path
from reader import Reader
from parser import Parser
from calculator import Calculator
from utils import print_most_humid_day, print_highest_temperature, print_lowest_temperature

if __name__ == '__main__':
    file_path = sys.argv[1]
    year = int(sys.argv[3])
    if (
            sys.argv[2] == '-e' and path.isdir(file_path) and Validator.year_validation(year, file_path)
    ):
        files_data_and_name = Reader.read_all_file(file_path)
        parsed_data = Parser.parser(files_data_and_name)
        calculator_instance = Calculator(parsed_data)

        max_temperature_data = calculator_instance.find_highest_in_year(year)
        print_highest_temperature(**max_temperature_data)

        min_temperature_data = calculator_instance.find_lowest_in_year(year)
        print_lowest_temperature(**min_temperature_data)

        max_humidity_data = calculator_instance.find_most_humid_in_year(year)
        print_most_humid_day(**max_humidity_data)
