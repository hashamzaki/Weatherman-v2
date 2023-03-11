import calendar
import sys

from constants import MapperIndex


def print_highest_temperature(max_temperature, month, day, year):
    print(f"Highest: {max_temperature}C on {calendar.month_abbr[month]} {day} {year}")


def print_lowest_temperature(min_temperature, month, day, year):
    print(f"Lowest: {min_temperature}C on {calendar.month_abbr[month]} {day} {year}")


def print_most_humid_day(max_humidity, month, day, year):
    print(f"Humidity: {max_humidity}% on {calendar.month_abbr[month]} {day} {year}")


def is_digit(value):
    return value.replace('-', '', 1).isdigit()


def is_float(value):
    return value.replace('.', '', 1).replace('-', '').isdigit()


def comparison_operation(operation_description, data_to_be_compared, comaring_value):
    if operation_description == MapperIndex.MAX_OPERATION_STRING:
        return_value = data_to_be_compared > comaring_value
    elif operation_description == MapperIndex.MIN_OPERATION_STRING:
        return_value = data_to_be_compared < comaring_value
    else:
        raise Exception('invalid argument')

    return return_value


def read_file_path():
    return sys.argv[1]


def read_switch():
    return sys.argv[2]


def read_year():
    return sys.argv[3]

