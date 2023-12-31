# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def simple_num(num):
    if num == 2 or num == 3: return True
    if num % 2 == 0 or num < 2: return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


number = int(input('Введите число от 0 до 100000 : '))
if 0 <= number <= 100000:
    print('Число простое - ' + str(simple_num(number)))
else:
    num = int(input('Введите число от 0 до 100000 : '))
