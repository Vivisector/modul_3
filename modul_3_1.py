# Переменная для подсчета вызовов
calls = 0

# Функция для подсчета вызовов
def count_calls():
    global calls
    calls += 1

# Функция для работы со строкой
def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    return (len(string), string.upper(), string.lower())

# Функция для проверки наличия строки в списке
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    # Приводим все к одному регистру для игнорирования регистра
    string = string.lower()
    normalized_list = [item.lower() for item in list_to_search]
    return string in normalized_list

# Примеры использования функций
result1 = string_info("Hello")
print("string_info('Hello'):", result1)

result2 = is_contains("Urban", ["city", "urban", "village"])
print("is_contains('Urban', ['city', 'urban', 'village']):", result2)

result3 = string_info("Python")
print("string_info('Python'):", result3)

result4 = is_contains("Tree", ["flower", "tree", "bush"])
print("is_contains('Tree', ['flower', 'tree', 'bush']):", result4)

# Выводим общее количество вызовов
print("Total calls to functions:", calls)
