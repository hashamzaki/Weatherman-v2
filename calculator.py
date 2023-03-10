from data_structures import WeatherData
from constants import MapperIndex
from utils import comparison_operation


class Calculator:

    def __init__(self,weather_data):
        self.weather_data: list(WeatherData) = weather_data

    @staticmethod
    def _year_and_data_validation(data_to_be_compared, data_year, input_year):
        return data_year == input_year and data_to_be_compared

    @staticmethod
    def _evaluate_operation_description(operation_description):
        if operation_description == 'max':
            comparing_value = float('-inf')
        elif operation_description == 'min':
            comparing_value = float('inf')
        else:
            raise Exception('invalid operation')

        return comparing_value

    def _description_based_value_evaluation(
            self, attribute_index, input_year,
            value_to_find_description, operation_description
    ):
        comparing_value = self._evaluate_operation_description(operation_description)
        day = ""
        month = ""
        for data in self.weather_data:
            data_to_be_compared = data.day_data[attribute_index]
            data_date = data.day_data[MapperIndex.DATE_INDEX]
            if (
                    self._year_and_data_validation(data_to_be_compared, data_date.year, input_year)
                    and comparison_operation(operation_description, data_to_be_compared, comparing_value)
            ):
                comparing_value = data_to_be_compared
                month = data_date.month
                day = data_date.day

        return {value_to_find_description: comparing_value, 'month': month, 'day': day}

    def find_highest_in_year(self, input_year):
        return self._description_based_value_evaluation(MapperIndex.MAX_TEMPERATURE,
                                                        input_year, 'max_temperature', 'max')

    def find_lowest_in_year(self, input_year):
        return self._description_based_value_evaluation(MapperIndex.MIN_TEMPERATURE,
                                                        input_year, 'min_temperature', 'min')

    def find_most_humid_in_year(self, input_year):
        return self._description_based_value_evaluation(MapperIndex.MAX_HUMIDITY,
                                                        input_year, 'max_humidity', 'max')

