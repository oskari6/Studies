import heapq

class Tasks:
    def __init__(self):
        self.heap = []
        self.task_map = {}

    def add_task(self, name, priority):
        self.task_map[name] = priority
        heapq.heappush(self.heap, (-priority, name))

    def fetch_task(self):
        while self.heap:
            neg_priority, name = heapq.heappop(self.heap)
            if name in self.task_map and self.task_map[name] == -neg_priority:
                del self.task_map[name]
                return name
        return None

if __name__ == "__main__":
    tasks = Tasks()

    tasks.add_task("siivous", 20)
    tasks.add_task("koodaus", 90)
    tasks.add_task("treffit", 80)

    print(tasks.fetch_task()) # koodaus

    tasks.add_task("nukkuminen", 20)

    print(tasks.fetch_task()) # treffit
    print(tasks.fetch_task()) # nukkuminen