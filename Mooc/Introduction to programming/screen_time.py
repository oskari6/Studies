from datetime import datetime, timedelta

filename = input("Filename:")
starting_date = input("Starting date:")
days = int(input("How many days:"))
print("Please type in screen time in minutes on each day (TV computer mobile):")

starting_date = datetime.strptime(starting_date, "%d.%m.%Y")

with open(filename, "w") as file:
    total_minutes = 0
    lines = []

    for i in range(days):
        current = starting_date + timedelta(days=i)
        screen_time = input(f"Screen time {current.strftime('%d.%m.%Y')}:")
        minutes = screen_time.split(" ")
        for entry in minutes:
            total_minutes += int(entry)
        lines.append(f"{current.strftime("%d.%m.%Y")}: {screen_time.replace(" ", "/")}")

    mean = total_minutes / days
    last_day = starting_date + timedelta(days=days-1)

    file.write(f"Time period: {starting_date.strftime('%d.%m.%Y')}-{last_day.strftime('%d.%m.%Y')}\n")
    file.write(f"Total minutes: {total_minutes}\n")
    file.write(f"Average minutes: {mean}\n")
    for line in lines:
        file.write(f"{line}\n")

print("Data stored in file late_june.txt")
