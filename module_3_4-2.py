import random
def get_fact(n):
    if n == 1:
        return n
    else:
        return n * get_fact(n - 1)

print(f'Простое перемножение цифр числа 5 [факториал]:', get_fact(5))


def get_multiplied_digits(str_num):
    if len(str_num) == 0:
        return 1
    first_digit = int(str_num[0])
    if first_digit == 0:
        return get_multiplied_digits(str_num[1:])
    else:
        return first_digit * get_multiplied_digits(str_num[1:])


def get_multiplied_digits2(str_num2): #вариант без проверки 0 или нет.
    if len(str(str_num2)) == 0:
        return 1
    first_digit = int(str(int(str_num2))[0])
    return first_digit * get_multiplied_digits2(str(int(str_num2))[1:])

str_num = str(40203)
str_num2 = str(190206508)

### генератор строки-числа
str_num3 = []
for i in range(int(input('введите число цифр для подсчета их произведения: '))):
    str_num3.append(str(random.choice(range(0,10))))
str_num3 = ''.join(str_num3)
### генератор строки-числа

result = get_multiplied_digits(str_num)
result2 = get_multiplied_digits2(str_num2)
result3 = get_multiplied_digits2(str_num3)
print(f'Произведение цифр числа {str_num} без учета нулей: {result}')
print(f'Произведение цифр числа {str_num2} без учета нулей: {result2}')
print(f'Произведение цифр числа {str_num3} без учета нулей: {result3}')
