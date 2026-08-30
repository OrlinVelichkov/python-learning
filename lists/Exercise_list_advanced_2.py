number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = list(filter(lambda x: x % 2 == 0, number))
print(new_list)
new_list2 = list(map(lambda x: x % 2 == 0, number))
print(new_list2)

def cars(car):
    if len(car) < 5:
        return True
    else:
        return False
my_garage = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan']
my_new_car = list(filter(cars, my_garage))
my_new_car2 = list(filter(lambda car: len(car) < 5, my_garage))
print(my_new_car)