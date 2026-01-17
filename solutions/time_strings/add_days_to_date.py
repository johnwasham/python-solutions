"""
You are given an initial date as a string in the format YYYY-MM-DD, along with an integer n which represents a number of days. Your task is to calculate the date after adding the given number of days to the initial date and return the result in the YYYY-MM-DD format.

Keep these points in mind when resolving the task:

The initial date string is always valid, formatted as YYYY-MM-DD, where YYYY denotes the year, MM the month, and DD the day.
The given integer n is the number of days you have to add to the initial date and will be up to 50,000.
The output should be a string showcasing the final date after adding n days, in the YYYY-MM-DD format.
Your function will be in the form add_days(date: str, n: int) -> str.

Constraints

date = the date string in the YYYY-MM-DD format. The year YYYY will be from 1900 to 2100, inclusive. The month MM and the day DD will be valid for the given year.
n = the integer representing the number of days you have to add to the initial date. n ranges from 1 to 50,000, inclusive.
You should consider leap years in the calculation. A year is a leap year if it is divisible by 4, but century years (years divisible by 100) are not leap years unless they are divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.
The month and day result should always be two digits long, padding with a 0 if necessary. For example, July 9th should be formatted as "07-09".
"""

from datetime import date, timedelta


def add_days(date_str, n):
    y, m, d = map(int, date_str.split('-'))
    start_date = date(y, m, d)

    new_date = start_date + timedelta(days=n)

    return format_date(new_date.year, new_date.month, new_date.day)


def format_date(year, month, day):
    return f"{year}-{month:02d}-{day:02d}"


assert add_days('1999-01-01', 365) == '2000-01-01'


    # year, month, day = date.split('-')
    # year = int(year)
    # month = int(month)
    # day = int(day)
    #
    # days_left = n
    #
    # print(year, month, day, n)
    #
    # # get days left in month
    # month_days = get_days_in_month(year, month)
    #
    # days_left_in_month = month_days - day
    # if days_left_in_month >= days_left:
    #     day = day + days_left
    #     return format_date(year, month, day)
    # else:
    #     days_left -= days_left_in_month
    #
    # print(year, month, day)
    #
    # # go month by month to end of year
    # for m in range(month + 1, 13):
    #     month_days = get_days_in_month(year, month)
    #     month = m
    #
    #     if month_days >= days_left:
    #         day = days_left
    #         return format_date(year, month, day)
    #     else:
    #         days_left -= month_days
    #
    # print(year, month, day)
    #
    # # go year by year (we are at dec 31)
    # while days_left >= 366:
    #     year += 1
    #     if is_leap_year(year):
    #         days_left -= 366
    #     else:
    #         days_left -= 365
    #
    # if days_left == 0:
    #     return format_date(year, month, day)
    #
    # # bump to jan 1
    # days_left -= 1
    # year += 1
    # month = 1
    # day = 1
    #
    # print(year, month, day, days_left)
    #
    # if days_left == 0:
    #     return format_date(year, month, day)
    #
    # # go month by month until nothing left
    # for m in range(1, 13):
    #     month_days = get_days_in_month(year, month)
    #     month = m
    #
    #     if month_days >= days_left:
    #         day = days_left
    #         return format_date(year, month, day)
    #     else:
    #         days_left -= month_days
    #
    # return format_date(year, month, day)


def format_date(year, month, day):
    return f"{year}-{month:02d}-{day:02d}"


# def get_days_in_month(year, month):
#     days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     month_days = days_in_month[month]
#     if month == 2 and is_leap_year(year):
#         month_days = 29
#
#     return month_days
#
#
# def is_leap_year(year):
#     if year % 100 == 0 and year % 400 == 0:
#         return True
#
#     return (year % 4 == 0)


assert add_days('1999-01-01', 365) == '2000-01-01'
assert add_days('1999-01-01', 366) == '2000-01-02'