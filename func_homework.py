# Создайте функции которые:
# умножают два числа
# складывают два числа
# делят числа между собой (НО!!! если делитель больше за делимое, проверяем внутри функции через if) тогда выводим
# предупреждение, если же все ок, делим!

def delenie(a, b):
    amount = a / b
    if a < b:
        print('Не делится')
    else:
        print(amount)

delenie(1,89)