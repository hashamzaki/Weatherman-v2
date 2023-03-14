import sys
from os import listdir, path
from utils import (
            comparison_operation, is_digit, read_sys_argument_year, read_sys_argument_file_path,
            type_cast_year, read_sys_argument_switch
)
from constants import MapperIndex,StringConstants


class InputValidator:
    @staticmethod
    def is_year_in_valid_range():
        input_year = type_cast_year(read_sys_argument_year())
        list_of_files = listdir(read_sys_argument_file_path())
        max_year = min_year = int(list_of_files[0].split('_')[MapperIndex.YEAR_IN_FILE_NAME])
        for file in list_of_files:
            file_year = int(file.split('_')[MapperIndex.YEAR_IN_FILE_NAME])
            if comparison_operation(StringConstants.MAX_OPERATION, file_year, max_year):
                max_year = file_year
            elif comparison_operation(StringConstants.MIN_OPERATION, file_year, min_year):
                min_year = file_year
            else:
                pass

        return min_year < input_year < max_year

    @staticmethod
    def is_argument_valid():
        return len(sys.argv) == MapperIndex.MAX_INPUT_ARGUMENT_LENGTH

    @staticmethod
    def is_dir():
        return path.isdir(read_sys_argument_file_path())

    @classmethod
    def is_year_valid(cls):
        if is_digit(read_sys_argument_year()):
            return cls.is_year_in_valid_range()
        else:
            return not read_sys_argument_year()
        
    @classmethod
    def yearly_data_calculation_conditions(cls):
        return (
                cls.is_argument_valid()
                and read_sys_argument_switch() == StringConstants.YEARLY_CALCULATION_SWITCH
                and cls.is_dir()
                and cls.is_year_valid()
        )

    @classmethod
    def all_year_data_calculation_conditions(cls):
        return (
                cls.is_argument_valid()
                and read_sys_argument_switch() == StringConstants.All_YEAR_CALCULATION_SWITCH
                and cls.is_dir()
                and cls.is_year_valid()
        )
