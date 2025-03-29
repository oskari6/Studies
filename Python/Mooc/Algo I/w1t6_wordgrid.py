class WordFinder:
    def set_grid(self, grid):
        self.grid = grid
    
    def count(self, word):
        grid = self.grid
        length = len(word)
        row_length = len(grid)
        column_length = len(grid[0])
        count = 0
        same = word == word[::-1]

        if len(word) == 1:
            return sum(row.count(word) for row in grid)

        for row in range(row_length):
            for i in range(column_length-length+1):
                if grid[row][i:i+length] == word:
                    count += 1
                if not same and grid[row][i:i+length][::-1] == word:
                    count += 1

        for col in range(column_length):
            vertical_string = ''.join(row[col] for row in grid)
            for i in range(row_length-length+1):
                if vertical_string[i:i+length] == word:
                    count += 1
                if not same and vertical_string[i:i+length][::-1] == word:
                    count += 1
        
        count += self.diagonal(word, same,)
        count += self.diagonal(word, same, right=False)

        return count

    def diagonal(self, word, same, right=True):
        grid = self.grid
        length = len(word)
        row_length = len(grid)
        column_length = len(grid[0])
        count = 0

        if right:
            for row in range(row_length-length+1):
                for col in range(column_length-length+1):
                    diagonal_string = ""
                    for i in range(length):
                        diagonal_string += grid[row+i][col+i]
                        if diagonal_string == word:
                            count += 1
                        if not same and diagonal_string[::-1] == word:
                            count += 1
        else:
            for row in range(row_length-length+1):
                for col in range(length-1, column_length):
                    diagonal_string = ""
                    for i in range(length):
                        diagonal_string += grid[row+i][col-i]
                        if diagonal_string == word:
                            count += 1
                        if not same and diagonal_string[::-1] == word:
                            count += 1
            
        return count



if __name__ == "__main__":
    grid = ["ECBD",
            "ADAC",
            "ACDE",
            "EDBA",
            "EEDB",
            "DABC"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("D"))
    print(finder.count("CE"))
    print(finder.count("CEA"))
    print(finder.count("EE"))
    print(finder.count("E"))

