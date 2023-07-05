# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint
lower_limit = 0
upper_limit = 1000
number_prompts = 10
num = randint(lower_limit, upper_limit)

for i in range(number_prompts):
    number = int(input('Введите ваше число: '))
    if number > num:
        print('Меньше')
    elif number < num:
        print('Больше')
    else:
        print('Угадали')
        break
print('Загаданное число было - ' + str(num))