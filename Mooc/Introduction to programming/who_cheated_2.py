from datetime import datetime, timedelta

def final_points():
    points = {}
    students = {}
    
    with open("start_times.csv") as file:
        for line in file:
            line = line.strip().split(";")
            name = line[0]
            deadline = datetime.strptime(line[1], "%H:%M") + timedelta(hours=3)
            students[name] = deadline

    with open("submissions.csv") as file:
        for line in file:
            line = line.strip().split(";")
            name = line[0]
            task = line[1]
            task_points = int(line[2])

            if name in students and datetime.strptime(line[3], "%H:%M") <= students[name]:
                if name not in points:
                    points[name] = {}
                if task not in points[name] or points[name][task] < task_points:
                    points[name][task] = task_points

            total = {student: sum(tasks.values()) for student, tasks in points.items()}
            
    return total

if __name__ == "__main__":
    points = final_points()
    print(points)