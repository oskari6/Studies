import urllib.request
import json

def retrieve_all():
    items = []
    response = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.loads(response.read())

    for item in data:
        if item.get("enabled", False):
            fullName = item.get("fullName", "N/A")
            name = item.get("name", "N/A")
            year = item.get("year", "N/A")
            sum_exercises = sum(item.get("exercises", []))
            line = (fullName, name, year, sum_exercises)
            items.append(line)
  
    return items

def retrieve_course(filename):
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{filename}/stats"
    items = {}
    response =  urllib.request.urlopen(url)
    data = json.loads(response.read())
    
    if not data:
        raise ValueError("No data received from the URL")
    
    data_list = list(data.values())

    if not data_list:
        raise ValueError("Parsed data is empty or invalid")
    
    weeks = len(data_list)
    max_students = max(item.get("students", 0) for item in data_list)
    hours = sum(item.get("hour_total", 0) for item in data_list)
    exercises = sum(item.get("exercise_total", 0) for item in data_list)

    for item in data_list:
        if item["students"] == max_students:
            students = item["students"]
            break

    items = {
        "weeks":weeks, 
        "students":students, 
        "hours":hours, 
        "hours_average":hours // students if students else 0, 
        "exercises":exercises, 
        "exercises_average":exercises // students if students else 0
    }

    return items

if __name__ == "__main__":
    stats1 = retrieve_all()
    print(stats1)
    stats = retrieve_course("docker2019")
    print(stats)