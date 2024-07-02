from math import inf

def my_divide(a, b):
    if b==0:
        # print('результат будет равен бесконечности')
        return inf

    res = a / b


    if isinstance(res, float):
        res = round(res, 2)

    return a, b, res


# a, b = int(input('ведите первое число:\n')), int(input('ведите второе число:\n'))
# a, b = 12, 0
# result = my_divide(a, b)
# if b!=0:
#     print(f'результат деления {a} на {b} равен {result}')
# else:
#     print(f'Делить на ноль нельзя, поэтому результат деления {a} на {b} будет бесконечно большим')