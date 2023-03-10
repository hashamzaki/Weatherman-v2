from os import listdir
from utils import comparison_operation
from constants import MapperIndex


class Validator:
    @staticmethod
    def year_validation(input_year, file_path):
        list_of_files = listdir(file_path)
        max_year = min_year = int(list_of_files[0].split('_')[MapperIndex.YEAR_IN_FILE_NAME])
        for file in list_of_files:
            file_year = int(file.split('_')[MapperIndex.YEAR_IN_FILE_NAME])
            if comparison_operation('max', file_year, max_year):
                max_year = file_year
            elif comparison_operation('min', file_year, min_year):
                min_year = file_year
            else:
                pass

        return not(input_year > max_year or input_year < min_year)
