import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    try:
        time1, time2 = s.split(" to ")
        if not (check_time(time1) and check_time(time2)):
            raise(ValueError)
    except ValueError:
        raise(ValueError)

    t1 = convert_to_24h(time1)
    t2 = convert_to_24h(time2)

    return f"{t1} to {t2}"

def check_time(time_str):
    pattern = r"^([1][0-2]|[0]?[1-9])(?::([0-5][0-9]))? (AM|PM)$"
    return bool(re.match(pattern, time_str))

def convert_to_24h(time_str):
    match = re.match(r"^([1][0-2]|[0]?[1-9])(?::([0-5][0-9]))? (AM|PM)$", time_str)
    if not match:
        raise ValueError("Invalid time format")

    hour = int(match.group(1))
    minute = int(match.group(2)) if match.group(2) else 0
    period = match.group(3)

    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
