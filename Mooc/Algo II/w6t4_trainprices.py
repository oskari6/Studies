class TrainPrices:
    def __init__(self):
        self.cities = []
        self.city_index = {}
        self.adjacency_matrix = []

    def add_city(self, name):
        if name not in self.city_index:
            self.city_index[name] = len(self.cities)
            self.cities.append(name)

            for row in self.adjacency_matrix:
                row.append(float("inf"))
            new_row = [float("inf")] * len(self.cities)
            new_row[-1] = 0
            self.adjacency_matrix.append(new_row)

    def add_train(self, city1, city2, price):
        i = self.city_index[city1]
        j = self.city_index[city2]
        self.adjacency_matrix[i][j] = price
        self.adjacency_matrix[j][i] = price


    def find_prices(self):
        n = len(self.cities)
        dist = [row[:] for row in self.adjacency_matrix]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        sorted_cities = sorted(self.cities)
        index_map = {name: i for i, name in enumerate(self.cities)}

        result = [[None] + sorted_cities]
        for i_name in sorted_cities:
            row = [i_name]
            i = index_map[i_name]
            for j_name in sorted_cities:
                j = index_map[j_name]
                cost = dist[i][j]
                row.append(int(cost) if cost != float("inf") else -1)
            result.append(row)

        return result

if __name__ == "__main__":
    prices = TrainPrices()

    prices.add_city("Helsinki")
    prices.add_city("Turku")
    prices.add_city("Tampere")
    prices.add_city("Oulu")

    prices.add_train("Helsinki", "Tampere", 20)
    prices.add_train("Helsinki", "Turku", 10)
    prices.add_train("Tampere", "Turku", 50)

    print(prices.find_prices())

    # the desired output:
    # [[None,       'Helsinki', 'Oulu', 'Tampere', 'Turku'],
    #  ['Helsinki', 0,          -1,     20,        10],
    #  ['Oulu',     -1,         0,      -1,        -1],
    #  ['Tampere',  20,         -1,     0,         30],
    #  ['Turku',    10,         -1,     30,        0]]