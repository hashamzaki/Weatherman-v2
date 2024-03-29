from data_structures import WeatherData
from constants import MapperIndex,StringConstants
from utils import comparison_operation


class Calculator:

    def __init__(self, weather_data):
        self.weather_data: list(WeatherData) = weather_data

    @staticmethod
    def _is_year_and_data_valid(data_to_be_compared, data_year, input_year):
        return data_year == input_year and data_to_be_compared

    @staticmethod
    def _evaluate_operation_description(operation_description):
        if operation_description == StringConstants.MAX_OPERATION:
            comparing_value = float('-inf')
        elif operation_description == StringConstants.MIN_OPERATION:
            comparing_value = float('inf')
        else:
            raise Exception('invalid operation')

        return comparing_value

    def _description_based_value_evaluation(
            self,
            attribute_index,
            input_year,
            value_to_find_description,
            operation_description
    ):
        comparing_value = self._evaluate_operation_description(operation_description)
        data_to_return = {}
        for data in self.weather_data:
            data_to_be_compared = data.day_data[attribute_index]
            data_date = data.day_data[MapperIndex.DATE_INDEX]
            if (
                not input_year
                and data_to_be_compared
                and comparison_operation(operation_description, data_to_be_compared, comparing_value)
            ):
                comparing_value = data_to_be_compared
                data_to_return = {
                    value_to_find_description: comparing_value,
                    'year': data_date.year,
                    'month': data_date.month,
                    'day': data_date.dayCalculat
                }

            elif (
                    self._is_year_and_data_valid(data_to_be_compared, data_date.year, input_year)
                    and comparison_operation(operation_description, data_to_be_compared, comparing_value)
            ):
                comparing_value = data_to_be_compared
                data_to_return = {
                    value_to_find_description: comparing_value,
                    'month': data_date.month,
                    'day': data_date.day,
                    'year': data_date.year
                }
            else:
                pass

        return data_to_return

    def find_highest(self, input_year):
        return self._description_based_value_evaluation(
            MapperIndex.MAX_TEMPERATURE,
            input_year, 'max_temperature',
            StringConstants.MAX_OPERATION
        )

    def find_lowest(self, input_year):
        return self._description_based_value_evaluation(
            MapperIndex.MIN_TEMPERATURE,
            input_year, 'min_temperature',
            StringConstants.MIN_OPERATION
        )

    def find_most_humid(self, input_year):
        return self._description_based_value_evaluation(
            MapperIndex.MAX_HUMIDITY,
            input_year, 'max_humidity',
            StringConstants.MAX_OPERATION
        )
