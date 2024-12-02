from datetime import datetime, timedelta

def cheaters():
    cheaters = []
    with open("start_times.csv") as file:
        for line in file:
            line = line.strip().split(";")
            name = line[0]
            deadline = datetime.strptime(line[1], "%H:%M") + timedelta(hours=3)
            with open("submissions.csv") as file:
                for line in file:
                    line = line.strip().split(";")
                    if line[0] == name:
                        if deadline < datetime.strptime(line[3], "%H:%M"):
                            cheaters.append(name)
                            break
    return cheaters

if __name__ == "__main__":
    cheats = cheaters()
    print(cheats)