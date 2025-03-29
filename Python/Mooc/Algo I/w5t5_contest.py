class Contest:
    entry_id = 1
    class Entry:
        def __init__(self, name, score, id):
            self.name = name
            self.score = score
            self.id = id

        def __lt__(self, other):
            if self.score == 0 and other.score == 0:
                return self.name < other.name
            if self.score == other.score:
                return self.id < other.id
            return self.score > other.score
            
        def __repr__(self):
            return f"({self.name}, {self.score}, {self.id})"

    def __init__(self, names, task_count):
        self.names = names
        self.task_count = task_count
        self.submissions = {}
        self.scoreboard = []
        
    def add_submission(self, name, task, score):
        key = (name, task)

        if key not in self.submissions or score > self.submissions[key].score:
            self.submissions[key] = self.Entry(name, score, Contest.entry_id)
            Contest.entry_id += 1

    def create_scoreboard(self):
        temp = {name: {"score": 0, "min_id": 1, "max_id": 1} for name in self.names}
        for entry in self.submissions.values():
            temp[entry.name]["score"] += entry.score
            temp[entry.name]["max_id"] = max(temp[entry.name]["max_id"], entry.id)

        self.scoreboard = [
            self.Entry(name, data["score"], data["max_id"]) for name, data in temp.items()
        ]
        self.scoreboard.sort()

        return [(entry.name, entry.score) for entry in self.scoreboard]

if __name__ == "__main__":
   names = ["pekka", "kalle", "anna", "eeva", "tiina"]
   contest = Contest(names, 5)

   contest.add_submission("tiina", 2, 41)
   contest.add_submission("pekka", 3, 41)

   scoreboard = contest.create_scoreboard()
   print(scoreboard)