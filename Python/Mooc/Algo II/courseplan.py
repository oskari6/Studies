class CoursePlan:
    def __init__(self):
        # TODO

    def add_course(self, course):
        # TODO

    def add_requisite(self, course1, course2):
        # TODO

    def find_order(self):
        # TODO

if __name__ == "__main__":
    courses = CoursePlan()

    courses.add_course("Ohpe")
    courses.add_course("Ohja")
    courses.add_course("Tira")
    courses.add_course("Jym")

    courses.add_requisite("Ohpe", "Ohja")
    courses.add_requisite("Ohja", "Tira")
    courses.add_requisite("Jym", "Tira")

    print(courses.find_order()) # esim. [Ohpe, Jym, Ohja, Tira]

    courses.add_requisite("Tira", "Tira")

    print(courses.find_order()) # None