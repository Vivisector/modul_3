def my_divide(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        res = 'деление на ноль запрещено'

    if isinstance(res, float):
        res = round(res, 2)

    # return a, b, res
    return res



# a, b = int(input('ведите первое число:\n')), int(input('ведите второе число:\n'))
# a, b = 12, 0
# result = my_divide(a, b)
# if b!=0:
#     print(f'результат деления {a} на {b} равен {result}')
# else:
#     print(f'{result}')