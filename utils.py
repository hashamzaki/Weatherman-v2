import calendar


def print_highest_temperature(max_temperature, month, day):
    print(f"Highest: {max_temperature}C on {calendar.month_abbr[month]} {day} ")


def print_lowest_temperature(min_temperature, month, day):
    print(f"Lowest: {min_temperature}C on {calendar.month_abbr[month]} {day}")


def print_most_humid_day(max_humidity, month, day):
    print(f"Humidity: {max_humidity}% on {calendar.month_abbr[month]} {day}")


def is_digit(value):
    return value.replace('-', '', 1).isdigit()


def is_float(value):
    return value.replace('.', '', 1).replace('-', '').isdigit()


def comparison_operation(operation_description, data_to_be_compared, comaring_value):
    if operation_description == 'max':
        return_value = data_to_be_compared > comaring_value
    elif operation_description == 'min':
        return_value = data_to_be_compared < comaring_value
    else:
        raise Exception('invalid argument')

    return return_value

