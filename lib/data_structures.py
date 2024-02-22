spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    nameList=[]
    for e in spicy_foods:
        nameList.append(e["name"])
    return nameList

print(get_names(spicy_foods))
def get_spiciest_foods(spicy_foods):
    food_list=[]
    for e in spicy_foods:
        if e["heat_level"]>5:
            food_list.append(e)
    return food_list

def print_spicy_foods(spicy_foods):
    spicy_emoji="🌶"
    for e in spicy_foods:
        print(f'{e["name"]} ({e["cuisine"]}) | Heat Level: {spicy_emoji*e["heat_level"]}')
    pass

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for e in spicy_foods:
        if cuisine==e["cuisine"]:
            return e
    pass

print(get_spicy_food_by_cuisine(spicy_foods,"American"))

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    l=len(spicy_foods)
    total=0
    for e in spicy_foods:
        total+=e["heat_level"]
    return total/l
    
print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy=[]
    for e in spicy_foods:
        new_spicy.append(e)
    new_spicy.append(spicy_food)
    return new_spicy
