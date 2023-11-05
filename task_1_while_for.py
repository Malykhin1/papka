n = int(input("Введите количество чисел: "))
numbers = []

for i in range(n):
    number = int(input("Введите число: "))
    numbers.append(number)

count_zero = numbers.count(0)
print("Количество нулей:", count_zero)