import sys
from inputvalidations import Validator
from os import path
from controller import Controller
from utils import is_digit

if __name__ == '__main__':
    file_path = sys.argv[1]
    year = sys.argv[3]
    year = int(year) if is_digit(year) else year
    if (
            path.isdir(file_path) and sys.argv[2] == '-e' and Validator.year_validation(year, file_path)
    ):
        Controller.print_yearly_data(file_path, year)
    elif path.isdir(file_path) and sys.argv[2] == '-a':
        Controller.print_yearly_data(file_path, year)
    else:
        raise Exception('invalid argument')

