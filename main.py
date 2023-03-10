import sys
from reader import Reader
from parser import Parser
from calculator import Calculator
from utils import print_most_humid_day, print_highest_temperature, print_lowest_temperature

if __name__ == '__main__':

    if sys.argv[1] == '-e':
        files_data_and_name = Reader.read_all_file('/home/faran/Downloads/weatherfiles (1)/weatherfiles')
        year = int(sys.argv[2])
        parsed_data = Parser.parser(files_data_and_name)
        
        calculator_instance = Calculator(parsed_data)
        max_temperature_data = calculator_instance.find_highest_in_year(year)
        print_highest_temperature(max_temperature_data)

        min_temperature_data = calculator_instance.find_lowest_in_year(year)
        print_lowest_temperature(min_temperature_data)

        max_humidity_data = calculator_instance.find_most_humid_in_year(year)
        print_most_humid_day(max_humidity_data)
