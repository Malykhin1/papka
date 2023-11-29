import random
n = 70
list = []

for i in range(n):
    num = random.randint(1, 31)
    list.append(num)

print(list)

list_sorted = sorted(list, reverse=False)
print(list_sorted)
