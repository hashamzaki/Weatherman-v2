from controller import Controller
from utils import read_sys_argument_file_path, read_sys_argument_year, type_cast_year
from validators import InputValidator
if __name__ == '__main__':
    if InputValidator.yearly_data_calculation_conditions():
        Controller.print_yearly_data(read_sys_argument_file_path(), type_cast_year(read_sys_argument_year()))
    elif InputValidator.all_year_data_calculation_conditions():
        Controller.print_yearly_data(read_sys_argument_file_path(), type_cast_year(read_sys_argument_year()))
    else:
        raise Exception('invalid argument')
