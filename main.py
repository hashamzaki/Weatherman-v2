from inputvalidations import Validator
from controller import Controller
from utils import read_file_path, read_year, read_switch, is_digit, typcast_year

if __name__ == '__main__':
    if (
            Validator.is_argument_valid() and read_switch() == '-e' and Validator.is_dir()
            and Validator.is_year_valid()
    ):
        year = typcast_year(read_year())
        file_path = read_file_path()
        Controller.print_yearly_data(file_path, year)
    elif (

            Validator.is_argument_valid() and read_switch() == '-a'
            and Validator.is_dir() and Validator.is_year_valid()
    ):
        year = typcast_year(read_year())
        file_path = read_file_path()
        Controller.print_yearly_data(file_path, year)
    else:
        raise Exception('invalid argument')

