class CoursePlan:
    def __init__(self):
        self.graph = {}
        self.in_degree = {}
        self.courses = set()

    def add_course(self, course):
        if course not in self.graph:
            self.graph[course] = []
        if course not in self.in_degree:
            self.in_degree[course] = 0
        self.courses.add(course)

    def add_requisite(self, course1, course2):
        if course1 == course2:
            self.courses.add(course1)
            self.graph.setdefault(course1, [])
            self.in_degree.setdefault(course1, 0)
            self.in_degree[course2] = self.in_degree.get(course2, 0) + 1
            return
        
        if course1 not in self.graph:
            self.graph[course1] = []
        if course2 not in self.graph:
            self.graph[course2] = []

        if course2 not in self.in_degree:
            self.in_degree[course1] = 0
        if course1 not in self.in_degree:
            self.in_degree[course2] = 0

        self.graph[course1].append(course2)
        self.in_degree[course2] += 1

        self.courses.add(course1)
        self.courses.add(course2)

    def find_order(self):
        local_in_degree = dict(self.in_degree)
        nothing_in_degree = [course for course in self.courses if local_in_degree[course] == 0]
        order = []

        while nothing_in_degree:
            course = nothing_in_degree.pop()
            order.append(course)

            for neighbor in self.graph.get(course, []):
                local_in_degree[neighbor] -= 1
                if local_in_degree[neighbor] == 0:
                    nothing_in_degree.append(neighbor)

        if len(order) == len(self.courses):
            return order
        return None

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