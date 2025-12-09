class Task:
    count = 0
    def __init__(self, description, programmer, workload):
        Task.count += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        self.id = Task.count

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        if self.finished:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders
    
    def programmers(self):
        programmers = []
        temp = set([order.programmer for order in self.orders])
        for item in temp:
            programmers.append(item)
        return programmers
    
    def mark_finished(self, id):
        orders = [order for order in self.orders if order.id == id]
        if orders:
            orders[0].mark_finished()
        else:
            raise ValueError()

    def finished_orders(self):
        return [task for task in self.orders if task.finished]
    
    def unfinished_orders(self):
        return [task for task in self.orders if not task.finished]

    def status_of_programmer(self, programmer):
        finished = 0
        unfinished = 0
        finished_work = 0
        unfinished_work = 0

        if programmer not in self.programmers():
            raise ValueError()
        
        for order in self.orders:
            if order.programmer == programmer:
                if order.is_finished():
                    finished += 1
                    finished_work += order.workload
                else:
                    unfinished += 1
                    unfinished_work += order.workload

        return (finished, unfinished, finished_work, unfinished_work)
    
if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
