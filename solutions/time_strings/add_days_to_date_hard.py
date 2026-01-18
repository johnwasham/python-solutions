def is_leap(year: int) -> bool:
    """Return True if year is a Gregorian leap year."""
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

def month_days(year: int, month: int) -> int:
    """Number of days in the given month of the given year."""
    if month == 2:
        return 29 if is_leap(year) else 28
    # April, June, September, November have 30 days
    if month in {4, 6, 9, 11}:
        return 30
    # All other months have 31 days
    return 31

def add_days(date_str: str, n: int) -> str:
    """Add `n` days to the date given by `date_str` (YYYY-MM-DD)."""
    y, m, d = map(int, date_str.split('-'))

    while n > 0:
        days_in_month = month_days(y, m)
        # How many days are left in the current month (including today)?
        remaining_in_month = days_in_month - d

        if n <= remaining_in_month:
            # The final day is within the current month
            d += n
            n = 0
        else:
            # Jump to the first day of the next month
            n -= (remaining_in_month + 1)   # skip to day 1 of next month
            d = 1
            if m == 12:
                m = 1
                y += 1
            else:
                m += 1

    return f"{y:04d}-{m:02d}-{d:02d}"