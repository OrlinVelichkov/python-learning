area = [1, 2, 3, 4, 5]
area1 = ['Banana', 'Apple', 'Lemon', 'Kiwi', 'Portocal', 'Grape']
area2 = [3.14, 5.85, 6.00, 12.9]
area3 = (111, 222, 333, 444, 555)
area4 = ['Audi', 'Ferrari', 'Lamroghini', 'Tesla', 'BYD']
area5 = list(area3)
print(area5)
area6 = list(map(float, area))
print(area6)
area7 = list(map(int, area2))
print(area7)
area1[2] = 'Ice Cream'
area1[-4:-1] = ['Fanta', 'Coca cola']
area1[1:3] = ['French fries', 'Beer']
area1[1:3] = 'Tarator', 'Salad'
print(area1)
new_area1 = area1[::]
new_area1[:2] = 'KFC',
print(new_area1)
new_area2 = new_area1.copy()
new_area2[1:1] = ['McDonalds']
print(new_area2)

my_garage = []
i = 0
while i < len(area4):
    my_garage.append(area4[i])
    i += 1
print(my_garage)

my_garage = []
while area4:
    my_garage.append(area4[0])
    area4.remove(area4[0]) 
print(my_garage)
area5 = list(range(1, 11, 3))
print(area5)
comprehension_area = [fruit for fruit in area1 if len(fruit) >=6]
comprehension_area = [fruit.upper() if fruit == 'Banana' else fruit.lower() for fruit in area1]
comprehension_area.sort(key=str.lower, reverse=True)
print(comprehension_area)
area11 = list(314)
print(area11)
adea_nova = input().split(', ')
print(adea_nova)
print(' and '.join(adea_nova))
new_ranklist = []
big500 = ['Nvidia', 'Anthropic', 'OpenAI', 'Meta', 'Google', 'SpaceX', 'Aetherith']
for company in big500:
    new_ranklist.append(company)
    new_ranklist.sort()
print(new_ranklist)
for position in range(len(big500)):
    new_ranklist.append(big500[position])
    new_ranklist.sort(key=lambda x: len(x) % 2 == 0, reverse=True)
print(new_ranklist)