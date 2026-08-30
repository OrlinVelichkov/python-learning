area = 'Python'
area2 = list(area)
print(area2)
print(''.join(area2))
area3 = input().split()
print(area3)
area4 = list(range(1, 10))
print(area4)
area5 = list(range(1, 10, 2))
print(area5)
area6 = list(range(10, 0, -1))
print(area6)
area7 = list(str(123456789))
print(area7)
area8 = list(map(float, input().split()))
print(area8)
area9 = list(map(int, input().split()))
print(area9)
area10 = list(map(str, input().split()))
area11 = list(map(bool, input().split()))
print(area10)
print(area11)
area12 = list(map(lambda x: x**2, range(1, 11)))
print(area12)

area13 = ['banana', 'apple', 'kiwi']
i = 0
area14 = []
while i < len(area13):
    area14.append(area13[i].upper())
    i += 1
print(area14)