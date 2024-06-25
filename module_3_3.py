def print_params(a=1, b='string', c=True):
    print(a,b,c)

print('печать с переданными параметрами:')
print_params(7, 'dfdfdf', 255)
print('печать без третьего переданного параметра:')
print_params(7, 'dfdfdf')

values_list = [14, 'mystring', [17, True, 'inline_string']]
values_list_short = [14, 'mystring']
values_dict= {'a': 700, 'b': 'another_string', 'c': False}
values_dict_short= {'c': False}

print('печать распакованного списка:')
print_params(*values_list)

print('печать распакованного словаря:')
print_params(**values_dict)

print('печать совмещенной распаковки:')
print_params(*values_list_short, **values_dict_short)

print('печать распаковки без третьего параметра (в третьем параметре будет напечатан третий параметр с умольчальным значением [c=True]:')
print_params(*values_list_short)

print('печать распаковки без первых двух параметров [подставятся умолчальные, определенные в самой функции]')
print_params(**values_dict_short)
