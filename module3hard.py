import sys

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def lister(element):
    sum_ = 0
    if isinstance(element, int):
        sum_ += element
    elif isinstance(element, str):
        sum_ += len(element)
    elif isinstance(element, (tuple, list, set)):
        for item in element:
            sum_ += lister(item)
    elif isinstance(element, dict):
        for key, val in element.items():
            sum_ += lister(key)
            sum_ += lister(val)

    return sum_


def calculate_structure_sum(data_structure):
    total = 0
    for el in data_structure:
        total += lister(el)
    return total

# result = calculate_structure_sum(data_structure)
print(calculate_structure_sum(data_structure))

# def lister_old(sum_, *args):
#     # if len(args) == 0: return sum_
#     for element in args:
#         if len(element) == 1:
#             # adder(sum_, element)
#             sum_ += element  # if isinstance(element, int) else len(element)
#             print(sum_)
#             return
#         else:
#             if isinstance(element, dict):
#                 for j, k in element.items():
#                     sum_ += j if isinstance(j, int) else len(j)
#                     sum_ += k if isinstance(j, int) else len(j)
#             else:
#                 for j in element:
#                     if isinstance(j, dict):
#                         for l, k in j.items():
#                             sum_ += l if isinstance(l, int) else len(l)
#                             sum_ += k if isinstance(k, int) else len(k)
#                     else:
#                         sum_ += j if isinstance(j, int) else len(j)
#                     # adder(sum_, j)
#     print(sum_)


# lister(0, *data_structure)
# print(sum_)
# sys.exit()

'''

def adder(sum_: 0, x):
    sum_ += x if isinstance(x, int) else len(x)
# temp_dict= (1, {'a': 4, 'b': 5}, 2)

for i in data_structure:

    # for i in temp_dict:
    if isinstance(i, dict):
        for j, k in i.items():
            # adder(sum_, j)
            # adder(sum_, k)
            sum += j if isinstance(j, int) else len(j)
            sum += k if isinstance(k, int) else len(k)
    else:
        for l in i:
            if type(l) is dict:
                for j, k in l.items():
                    # adder(sum_, j)
                    # adder(sum_, k)
                    sum += j if isinstance(j, int) else len(j)
                    sum += k if isinstance(k, int) else len(k)
            else:
                # adder(sum_, l)
                sum += l if isinstance(l, int) else len(l)

'''
