"""
You are given two input arguments: an array of strings timePoints and an integer added_seconds. Each string in timePoints is in the HH:MM:SS format, representing a valid time from "00:00:00" to "23:59:59" inclusive. The integer added_seconds represents a number of seconds, ranging from 1 to 86,400. Your task is to create a new function, add_seconds_to_times(timePoints, added_seconds), which takes these two arguments and returns a new array of strings. Each string in the returned array is the new time, calculated by adding the provided added_seconds to the corresponding time in timePoints, formatted in HH:MM:SS.

The array timePoints contains n strings, where n can be any integer from 1 to 100 inclusive. The time represented by each string in timePoints is guaranteed to be valid. The total time, after adding added_seconds, can roll over to the next day.

Example

For timePoints = ['10:00:00', '23:30:00'] and added_seconds = 3600, the output should be ['11:00:00', '00:30:00'].
"""


def add_seconds_to_times(time_points, added_seconds):
    results = []

    for time_point in time_points:
        hours, minutes, seconds = time_point.split(':')
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)

        seconds_since_start = hours * 3600 + minutes * 60 + seconds
        seconds_since_start = (seconds_since_start + added_seconds) % (24 * 3600)
        hours, remainder = divmod(seconds_since_start, 3600)
        minutes, seconds = divmod(remainder, 60)

        results.append(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    return results


assert add_seconds_to_times(['10:00:00', '23:30:00'], 3600) == ['11:00:00', '00:30:00']