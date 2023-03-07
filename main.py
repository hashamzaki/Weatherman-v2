import sys
from reader import Reader
from parser import Parser

if __name__ == '__main__':

    if sys.argv[1] == '-e':
        files_data = Reader().read_all_file('/home/faran/Downloads/weatherfiles (1)/weatherfiles')
        calculation_instance = Parser().parser(files_data)
        calculation_instance.find_highest_in_year()
        calculation_instance.find_lowest_in_year()
        calculation_instance.find_most_humid_in_year()


