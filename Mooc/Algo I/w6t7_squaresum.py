class DataAnalyzer:
    def __init__(self):
        self.n = 0
        self.sum_x = 0
        self.sum_y = 0
        self.sum_x2 = 0
        self.sum_y2 = 0
        self.sum_xy = 0

    def add_point(self, x, y):
        self.n += 1
        self.sum_x += x
        self.sum_y += y
        self.sum_x2 += x**2
        self.sum_y2 += y**2
        self.sum_xy += x*y

    def calculate_error(self, a, b):
        # returning the simplified equation. 
        return (
            self.sum_y2
            - 2 * a * self.sum_xy
            - 2 * b * self.sum_y
            + a**2 * self.sum_x2
            + 2 * a * b * self.sum_x
            + self.n * b **2
        )

if __name__ == "__main__":
    analyzer = DataAnalyzer()

    analyzer.add_point(1, 1)
    analyzer.add_point(3, 2)
    analyzer.add_point(5, 3)
    print(analyzer.calculate_error(1, 0)) # 5
    print(analyzer.calculate_error(1, -1)) # 2
    print(analyzer.calculate_error(3, 2)) # 293

    analyzer.add_point(4, 2)
    print(analyzer.calculate_error(1, 0)) # 9
    print(analyzer.calculate_error(1, -1)) # 3
    print(analyzer.calculate_error(3, 2)) # 437