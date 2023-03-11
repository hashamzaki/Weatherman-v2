from reader import Reader
from parser import Parser
from calculator import Calculator
from utils import print_most_humid_day, print_highest_temperature, print_lowest_temperature


class Controller:
    @staticmethod
    def print_yearly_data(file_path, year):
        files_data_and_name = Reader.read_all_file(file_path)
        parsed_data = Parser.parser(files_data_and_name)
        calculator_instance = Calculator(parsed_data)

        max_temperature_data = calculator_instance.find_highest_(year)
        print_highest_temperature(**max_temperature_data)

        min_temperature_data = calculator_instance.find_lowest_(year)
        print_lowest_temperature(**min_temperature_data)

        max_humidity_data = calculator_instance.find_most_humid_(year)
        print_most_humid_day(**max_humidity_data)
