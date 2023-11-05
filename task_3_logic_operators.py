sum_investions = int(input('Минимальная сумма инвестиций: '))
cash_ivan = int(input('Денег у Ивана: '))
cash_michael = int(input('Денег у Майкла : '))
if sum_investions <= cash_ivan and sum_investions <= cash_michael:
    print('2')
elif sum_investions <= cash_ivan and sum_investions >= cash_michael:
    print('1')
elif sum_investions >= cash_ivan and sum_investions <= cash_michael:
    print('1')
else:
    print('0')