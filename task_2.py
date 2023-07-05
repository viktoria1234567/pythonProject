# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
num = int(input('Введите число от 1 до 999: '))
num_str = str(num)
mult = 1
digit = 0
result = ''
if 1 <= num <= 999:
    if len(num_str) == 1:
        print(num**2)
    elif len(num_str) == 2:
        while num > 0:
            digit = num % 10
            mult = mult * digit
            num = num // 10
        print(mult)
    elif len(num_str) == 3:
        while num > 0:
            digit = str(num % 10)
            result = result + digit
            num = num // 10
        print(int(result))
else:
    num = int(input('Введите число от 1 до 999: '))
