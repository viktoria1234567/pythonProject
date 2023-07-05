# Напишите программу, которая запрашивает год и проверяет его на високосность.

reform = 1582
small_leap_year = 4
not_leap_year = 100
big_leap_year = 400

year = int(input('Введите год в формате yyyy: '))
if year >= reform:
    if year % small_leap_year != 0:
        result = "Обычный"
    elif year % not_leap_year == 0:
        if year % big_leap_year == 0:
            result ="Високосный"
        else:
            result ="Обычный"
    else:
        result ="Високосный"
elif year % small_leap_year != 0:
    result ="Обычный"
else:
    result ="Високосный"

print(result)