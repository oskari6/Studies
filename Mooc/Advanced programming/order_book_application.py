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

class OrderBookApp:
    def __init__(self):
        self.orderbook = OrderBook()

    def execute_order(self):
            desc = input("description:")
            estimate = input("programmer and workload estimate:")
            if " " not in estimate:
                print("erroneous input")
                return
            programmer, workload = estimate.split(" ")
            try:
                workload = int(workload)
            except ValueError:
                print("erroneous input")
                return
            
            self.orderbook.orders.append(Task(desc, programmer, workload))
            print("added!")
    
    def execute_finished(self):
        finished = self.orderbook.finished_orders()
        if finished:
            for order in finished:
                print(order)
        else:
            print("no finished tasks")

    def execute_unfinished(self):
        unfinished = self.orderbook.orders
        if unfinished:
            for order in unfinished:
                print(order)
        else:
            print("no unfinished tasks")

    def execute_marked(self):
        try:
            id = int(input("id:"))
        except ValueError:
            print("erroneous input")
            return
        try:
            self.orderbook.mark_finished(id)
            print("marked as finished")
        except ValueError:
            print("erroneous input")

    def execute_programmers(self):
        programmers = self.orderbook.programmers()
        if programmers:
            for programmer in programmers:
                print(programmer)
        else:
            print("no programmers")

    def execute_status(self):
        programmer = input("programmer:")
        try:
            finished_orders = 0
            unfinished_orders = 0
            finished_work = 0
            unfinished_work = 0

            orders = self.orderbook.all_orders()
            if not any(order.programmer == programmer for order in orders):
                raise ValueError("erroneous input")
            
            has_work = False
            for order in orders:
                if order.programmer == programmer:
                    has_work = True
                    if order.finished:
                        finished_orders += 1
                        finished_work += order.workload
                    else:
                        unfinished_orders += 1
                        unfinished_work += order.workload
            print(f"tasks: finished {finished_orders} not finished {unfinished_orders}, hours: done {finished_work} scheduled {unfinished_work}")

        except ValueError:
            print("erroneous input")
    
    def execute(self):
        print("commands:")
        while True:
            print("0 exit")
            print("1 add order")
            print("2 list finished tasks")
            print("3 list unfinished tasks")
            print("4 mark task as finished")
            print("5 programmers")
            print("6 status of programmer")
            num = int(input("command:"))
            if num == 0:
                break
            elif num == 1:
                self.execute_order()
            elif num == 2:
                self.execute_finished()
            elif num == 3:
                self.execute_unfinished()
            elif num == 4:
                self.execute_marked()
            elif num == 5:
                self.execute_programmers()
            elif num == 6:
                self.execute_status()
            else:
                continue

app = OrderBookApp()
app.execute()