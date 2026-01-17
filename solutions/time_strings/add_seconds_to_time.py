def add_seconds(s, seconds):
    hours, mins, secs = s.split(":")

    hours = int(hours)
    mins = int(mins)
    secs = int(secs)

    seconds_since_start = hours * 3600 + mins * 60 + secs

    total_seconds = (seconds_since_start + seconds) % (24 * 3600)

    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


assert add_seconds("05:24:36", 123) == "05:26:39"
assert add_seconds("23:15:56", 2800) == "00:02:36"