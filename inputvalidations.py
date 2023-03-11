import sys
from os import listdir,path
from utils import comparison_operation, is_digit, read_year, read_file_path,typcast_year
from constants import MapperIndex


class Validator:
    @staticmethod
    def is_year_in_valid_range():
        input_year = typcast_year(read_year())
        list_of_files = listdir(read_file_path())
        max_year = min_year = int(list_of_files[0].split('_')[MapperIndex.YEAR_IN_FILE_NAME])
        for file in list_of_files:
            file_year = int(file.split('_')[MapperIndex.YEAR_IN_FILE_NAME])
            if comparison_operation(MapperIndex.MAX_OPERATION_STRING, file_year, max_year):
                max_year = file_year
            elif comparison_operation(MapperIndex.MIN_OPERATION_STRING, file_year, min_year):
                min_year = file_year
            else:
                pass

        return min_year < input_year < max_year

    @staticmethod
    def is_argument_valid():
        return True if len(sys.argv) == 4 else False

    @staticmethod
    def is_dir():
        return True if path.isdir(read_file_path()) else False

    @classmethod
    def is_year_valid(cls):
        return cls.is_year_in_valid_range() if is_digit(read_year()) else True if not read_year() else False
