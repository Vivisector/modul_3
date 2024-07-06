data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def f(data):
    if isinstance(data, int): return data
    elif isinstance(data, str): return len(data)
    elif isinstance(data, (tuple, list, set)): return sum([f(x) for x in data])
    else: return sum ([f(k) + f(v) for k, v in data.items()])

print(f(data_structure))