def search_by_name(filename, word):
    recipes = get_recipes(filename)
    wanted = []
    for names in recipes:
        if word.lower() in names[0].lower():
            wanted.append(names[0])
    return wanted

def search_by_time(filename, prep_time):
    recipes = get_recipes(filename)
    wanted = []
    for times in recipes:
        if prep_time >= int(times[1]):
            wanted.append(times[0] + f", preparation time {times[1]} min")
    return wanted

def search_by_ingredient(filename, ingredient):
    recipes = get_recipes(filename)
    wanted = []
    for recipe in recipes:
        for word in recipe:
            if ingredient == word:
                wanted.append(recipe[0] + f", preparation time {recipe[1]} min")
    return wanted

def get_recipes(filename):    
    with open(filename) as file:
        recipes = []
        current_recipe = []
        for line in file:
            stripped_line = line.strip()
            if stripped_line == "":
                if current_recipe:  # Check if there is something in the current recipe
                    recipes.append(current_recipe)
                    current_recipe = []
            else:
                current_recipe.append(stripped_line)

        # Append the last recipe if the file doesn't end with a blank line
        if current_recipe:
            recipes.append(current_recipe)
    return recipes


if __name__ == "__main__":
    name = input("File:")
    recipe = input("recipe:")
    by_name = search_by_name("recipes1.txt", "cake")
    timed = search_by_time("recipes1.txt", 20)
    for item in by_name:
        print(item)
    print(timed)
    found_recipes = search_by_ingredient("recipes1.txt", "milk")
    for recipe in found_recipes:
        print(recipe)