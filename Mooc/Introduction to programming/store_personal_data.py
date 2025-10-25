def store_personal_data(person):
    name, age, height = person
    with open("people.csv", "a") as file:
        file.write(name+";"+str(age)+";"+str(height)+"\n")

if __name__ == "__main__":
    name ="Paul Palson"
    age =37
    height= 175.5
    person = name, age, height
    store_personal_data(person)