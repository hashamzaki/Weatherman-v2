import calendar


def print_highest_temperature(max_temperature, month, day):
    print(f"Highest: {max_temperature}C on {calendar.month_abbr[month]} {day} ")


def print_lowest_temperature(min_temperature, month, day):
    print(f"Lowest: {min_temperature}C on {calendar.month_abbr[month]} {day} ")


def print_most_humid_day(max_humidity, month, day):
    print(f"Humidity: {max_humidity}% on {calendar.month_abbr[month]} {day} ")


def is_digit(value):
    if value.replace('-', '').isdigit():
        return True
    else:
        return False


def is_float(value):
    if value.replace('.', '', 1).replace('-', '').isdigit():
        return True
    else:
        return False
