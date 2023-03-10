import data_structures


class Calculator:

    def __init__(self,weather_data):
        self.weather_data: list(data_structures.WeatherData)=weather_data

    @staticmethod
    def _year_and_data_validation(data_to_be_compared, data_year, year_to_be_compared):
        return True if data_year == year_to_be_compared and data_to_be_compared else False

    @staticmethod
    def _comparison_operation(operation_description, data_to_be_compared, value):
        if operation_description == 'max':
            return True if data_to_be_compared > value else False
        elif operation_description == 'min':
            return True if data_to_be_compared < value else False
        else:
            raise Exception('invalid argument')

    def _description_based_value_evaluation(
            self, index, year_to_be_compared,
            value_to_find_description, operation_description
    ):
        if operation_description == 'max':
            comparing_value = float('-inf')
        elif operation_description == 'min':
            comparing_value = float('inf')
        else:
            raise Exception('invalid operation')
        day = ""
        month = ""
        for data in self.weather_data:
            data_to_be_compared = data.day_data[index]
            if (
                    self._year_and_data_validation(data_to_be_compared, data.day_data[0].year, year_to_be_compared)
                    and self._comparison_operation(operation_description, data_to_be_compared, comparing_value)
            ):
                comparing_value = data_to_be_compared
                month = data.day_data[0].month
                day = data.day_data[0].day

        return {value_to_find_description: comparing_value, 'month': month, 'day': day}

    def find_highest_in_year(self, year_to_be_compared):
        return self._description_based_value_evaluation(1, year_to_be_compared, 'max_temperature', 'max')

    def find_lowest_in_year(self, year_to_be_compared):
        return self._description_based_value_evaluation(3, year_to_be_compared, 'min_temperature', 'min')

    def find_most_humid_in_year(self, year_to_be_compared):
        return self._description_based_value_evaluation(8, year_to_be_compared, 'max_humidity','max')

