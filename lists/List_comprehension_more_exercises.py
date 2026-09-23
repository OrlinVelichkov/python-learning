#exercise for nested list comprehension
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
new_data = [x for row in data for x in row]
print(new_data)
new_data2 = [[name for name in names] for row in data]
new_data3 = [[str(x) for x in row] for row in data]
print(new_data2)
print(new_data3)
