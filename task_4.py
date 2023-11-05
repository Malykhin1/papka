number = int(input("Введите пятизначное целое число: "))
units = number % 10
tens = number % 100 // 10
hundreds = number % 1000 // 100
thousands = number % 10000 // 1000
tens_of_thous = number // 10000
print((tens ** units) * hundreds / (tens_of_thous - thousands))

#ссылка на репозиторий в GitHub: https://github.com/Malykhin1/python_tasks
