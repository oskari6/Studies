def filter_solutions():
    correct = []
    incorrect = []
    with open("solutions.csv") as file:
        for line in file:
            line = line.strip().split(";")
            result = eval(line[1])
            if result == int(line[2]):
                correct.append(line)
            else:
                incorrect.append(line)
    with open("correct.csv", "w") as file2:
        for item in correct:
            file2.write(";".join(item)+"\n")

    with open("incorrect.csv", "w") as file3:
        for item in incorrect:
            file3.write(";".join(item) +"\n" )
    file.close()
    file2.close()
    file3.close()

if __name__ == "__main__":
    filter_solutions()