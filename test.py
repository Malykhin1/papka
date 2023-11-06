num = int(input('Введите целое число: '))

if num == 0:
    print('Число равно 0')
elif num > 0 and num % 2 == 0:
    print('Это положительное четное число')
elif num < 0 and num % 2 == 0:
    print('Это отрицательное четное число')
elif num > 0 and num % 2 != 0:
    print('Это положительное нечетное число')
else:
    print('Это отрицательное нечетное число')

import subprocess
import os

while True:
    process = subprocess.Popen(['python', 'test.py'])
    process.wait()
    if process.returncode != 0:
        break