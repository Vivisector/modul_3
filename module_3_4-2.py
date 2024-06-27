import sys

# print('string'[1:])
# sys.exit()
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
result = get_multiplied_digits(str_num)
result2 = get_multiplied_digits2(str_num2)
print(f'Произведение цифр числа {str_num} без учета нулей: {result}')
print(f'Произведение цифр числа {str_num2} без учета нулей: {result2}')
