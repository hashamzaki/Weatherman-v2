
class Calculator:
    @staticmethod
    def __year_and_data_validation(data_to_be_compared, data_year, year_to_be_compared):
        if (
                data_year == year_to_be_compared
                and data_to_be_compared
        ):
            return True
        else:
            return False

    @staticmethod
    def __comparison_operation(operation_description, data_to_be_compared, value):
        if operation_description == 'max':
            if data_to_be_compared > value:
                return True
            else:
                return False
        else:
            if data_to_be_compared < value:
                return True
            else:
                return False

    @classmethod
    def __find_highest_value_based_on_index(
                cls, index, weather_data, year_to_be_compared, 
            value_to_find_description, operation_description
    ):
        if operation_description == 'max':
            comparing_value = float('-inf')
        else:
            comparing_value = float('inf')
        day = ""
        month = ""
        for data in weather_data:
            data_to_be_compared = data.day_data[index]
            if (
                    cls.__year_and_data_validation(data_to_be_compared, data.day_data[0].year, year_to_be_compared)
                    and cls.__comparison_operation(operation_description, data_to_be_compared, comparing_value)
            ):
                comparing_value = data_to_be_compared
                month = data.day_data[0].month
                day = data.day_data[0].day

        return {value_to_find_description: comparing_value, 'month': month, 'day': day}

    @classmethod
    def find_highest_in_year(cls, weather_data, year_to_be_compared):
        return cls.__find_highest_value_based_on_index(1,weather_data, year_to_be_compared, 'max_temperature', 'max')

    @classmethod
    def find_lowest_in_year(cls, weather_data, year_to_be_compared):
        return cls.__find_highest_value_based_on_index(3, weather_data, year_to_be_compared, 'min_temperature', 'min')

    @classmethod
    def find_most_humid_in_year(cls, weather_data, year_to_be_compared):
        return cls.__find_highest_value_based_on_index(8, weather_data, year_to_be_compared, 'max_humidity','max')

