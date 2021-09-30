import calendar
from datetime import datetime, timedelta

WEEKDAY_NAME_LIST = list(calendar.day_name)


def add_time(start_time, duration, start_day_name=None):
    # Parsing "start_time" parameter's hours and miniutes values and,
    #   creating datetime obj with those data.
    parsed_start_datetime = datetime.strptime(start_time, "%I:%M %p")
    current_datetime = datetime.now()
    start_datetime = current_datetime.replace(
        hour=parsed_start_datetime.hour,
        minute=parsed_start_datetime.minute,
        second=0,
        microsecond=0,
    )

    # Manually parsing "duration" param's hours and miniutes values and,
    #   creating timedelta obj with those data.
    duration_hours, duration_minutes = duration.split(":")
    duration_delta = timedelta(
        hours=int(duration_hours),
        minutes=int(duration_minutes),
    )

    # New datetime object witch point to future date. (According to provided duration.)
    future_datetime = start_datetime + duration_delta

    # Calculating how many days to future date.
    duration_diff_as_days = duration_delta.days
    if duration_delta.days > 0 and duration_delta.seconds > 0:
        # When there is some days + hours available.
        duration_diff_as_days = duration_delta.days + 1

    # Custom string, that show in how many days, future day occur.
    custom_duration_representation = ""
    if duration_diff_as_days == 0 and start_datetime.day != future_datetime.day:
        # When there is no 24 Hour difference, But hour difference pass above 12:00 PM which makes it next day.
        custom_duration_representation = " (next day)"
    elif duration_diff_as_days == 1:
        custom_duration_representation = " (next day)"
    elif duration_diff_as_days > 1:
        custom_duration_representation = (
            f" ({duration_diff_as_days} days later)"
        )

    # When custom start date is proviced (If not default is considered today),
    #   in here we calculate in which week day name, future day will be.
    if start_day_name is not None:
        start_day_index = WEEKDAY_NAME_LIST.index(start_day_name.title())
        future_day_index = (start_day_index + duration_diff_as_days) % 7
        custom_duration_representation = (
            ", "
            + WEEKDAY_NAME_LIST[future_day_index]
            + custom_duration_representation
        )

    # Formatting future date in certain format.
    return future_datetime.strftime(
        f"%-I:%M %p{custom_duration_representation}"
    )
