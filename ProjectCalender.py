import calendar

def is_leap(year):
    """Return True if leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def display_year_calendar(year):
    """Print the full calendar for the given year."""
    print("=" * 400)
