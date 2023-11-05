number = int(input("Введите пятизначное целое число: "))
units = number % 10
dozens = number % 100 // 10
hundreds = number % 1000 // 100
thousands = number % 10000 // 1000
doz_of_thous = number // 10000
print((dozens ** units) * hundreds / (doz_of_thous - thousands))

#ссылка на репозиторий в GitHub: https://github.com/Malykhin1/python_tasks
