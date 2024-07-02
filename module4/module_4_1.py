import math
from true_math import my_divide as my_t
from fake_math import my_divide as my_f

a, b = 154, 0

resultT = my_t(a, b)
resultF = my_f(a, b)
if b!=0:
    print(f'При делении {a} на {b} получится: {resultF}')
else:
    print(f'Фейковая математика при делении на ноль укажет, что деление {a} на {b} даст ошибку - {resultF}')
    print(f'А истинная математика при делении на ноль просто скажет, что {a} делить на {b} будет бесконечность ({resultT})')
