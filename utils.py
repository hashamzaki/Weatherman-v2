import calendar


def print_highest_temperature(data_to_print):
    print(f"Highest: {data_to_print['max_temperature']}C on {calendar.month_abbr[data_to_print['month']]} "
          f"{data_to_print['day']} ")


def print_lowest_temperature(data_to_print):
    print(f"Lowest: {data_to_print['min_temperature']}C on {calendar.month_abbr[data_to_print['month']]} "
          f"{data_to_print['day']} ")


def print_most_humid_day(data_to_print):
    print(f"Humidity: {data_to_print['max_humidity']}% on {calendar.month_abbr[data_to_print['month']]} "
          f"{data_to_print['day']} ")


def is_digit(value):
    return True if value.replace('-', '').isdigit() else False


def is_float(value):
    return True if value.replace('.', '', 1).replace('-', '').isdigit() else False
