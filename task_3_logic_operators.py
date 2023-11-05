sum_investions = int(input('Минимальная сумма инвестиций: '))
cash_ivan = int(input('Денег у Ивана: '))
cash_michael = int(input('Денег у Майкла : '))
if sum_investions <= cash_ivan and sum_investions <= cash_michael:
    print('Вложиться могут: 2')
elif sum_investions <= cash_ivan and sum_investions >= cash_michael:
    print('Вложиться могут: 1')
elif sum_investions >= cash_ivan and sum_investions <= cash_michael:
    print('Вложиться могут: 1')
else:
    print('Вложиться не могут')

#ссылка на репозиторий в GitHub: https://github.com/Malykhin1/python_tasks