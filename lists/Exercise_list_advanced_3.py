# 🥊 Mission 4 — Dynamic Positions
products = [
    "Keyboard",
    "Mouse",
    "Monitor",
    "Laptop",
    "Webcam",
    "Headphones",
    "USB Hub"
]
last_index = len(products)-1
middle_index = len(products)//2
print(products[0])
print(products[last_index])
print(products[middle_index])


# 🥊 Mission 5 — Mini Stage 3 Checkpoint
temperatures = [18, 21, 24, 27, 30, 26, 22, 19, 17]
print(temperatures[0])
print(temperatures[1])
print(temperatures[-1])
print(temperatures[-3])
print(temperatures[len(temperatures) // 2])
print(temperatures[len(temperatures) -1 ])


bulgarian_cities = ['Sofia', 'Plovdiv', 'Varna', 'Burgas', 'Ruse', 'Stara Zagora', 'Pleven', 'Sliven', 'Dobrich', 'Shumen']
last_city = bulgarian_cities[len(bulgarian_cities) - 1]
last_city_index = len(bulgarian_cities) - 1
middle_city = bulgarian_cities[len(bulgarian_cities) // 2]
middle_city_index = len(bulgarian_cities) // 2
middle_char_middle_city = bulgarian_cities[len(bulgarian_cities) // 2][len(bulgarian_cities[len(bulgarian_cities) //2]) // 2]

print(bulgarian_cities[last_city_index])
print(bulgarian_cities[middle_city_index])
print(middle_char_middle_city)
numbers = [10, 20, 30, 40]
numbers[1:3] = 999,
print(numbers)

# 🥊 Mission 1 — Single Mutation
colors = ["red", "green", "blue", "yellow"]
colors[1] = 'lime'
print(colors)

# 🥊 Mission 2 — Negative Mutation
scores = [50, 60, 70, 80]
scores[-1] = 100
print(scores)
# 🥊 Mission 3 — Dynamic Mutation
temperatures = [18, 21, 24, 27, 30]
last_index = len(temperatures) - 1
temperatures[last_index] = 25
print(temperatures)
# 🥊 Mission 4 — Slice Replacement
numbers = [10, 20, 30, 40, 50]
numbers[1:3] = [200, 300]
print(numbers)
# 🥊 Mission 5 — Slice Insertion
products = ["Keyboard", "Monitor", "Laptop"]
products[1:1] = ['Mouse']
print(products)
# 🥊 Mission 6 — Dynamic End Insertion
cities = ["Sofia", "Plovdiv", "Varna"]
cities[len(cities):len(cities)] = ['Burgas']
print(cities)
# 🥊 Mission 7 — Mini Checkpoint
data = [10, 20, 30, 40, 50]
data[0] = 100
data[-1] = 500
data[1:3] = [200, 300]
data[2:2] = [250]
data[len(data):len(data)] = [600]
print(data)