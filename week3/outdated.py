months = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            try:
                m, d, y = map(int, date.split("/"))
            except ValueError:
                pass

        elif "," in date:
            month_name, rest = date.split(" ", 1)
            d, y = rest.replace(",", "").split()

            for month in months:
                if (month == month_name):
                    m = months[month_name]
                    d = int(d)
                    y = int(y)
        else:
            continue

        try:
            if (1 <= m <= 12 and 1 <= d <= 31):
                print(f"{y}-{m:02}-{d:02}")
                break
        except NameError:
            pass

    except KeyboardInterrupt:
        break

    except EOFError:
        break

print("")