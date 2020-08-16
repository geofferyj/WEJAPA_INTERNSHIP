def readable_timedelta(days):
    # insert your docstring here
    """ function to convert ints to date format

    Args:
        days (int): number to convert

    Returns:
        str: converted data in a sentence
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)