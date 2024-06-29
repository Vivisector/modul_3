import tkinter as tk

def get_values():
    try:
        num1 = int(number1_entry.get())
        num2 = int(number2_entry.get())
        return num1, num2
    except ValueError:
        insert_values("Error: non-integer input")
        return None, None

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def calculate(operation):
    num1, num2 = get_values()
    if num1 is None or num2 is None:
        return
    if operation == 'СУМ':
        res = num1 + num2
    elif operation == 'ВЫЧ':
        res = num1 - num2
    elif operation == 'УМН':
        res = num1 * num2
    elif operation == 'ДЕЛ':
        if num2 == 0:
            insert_values("Error: div by 0")
            return
        res = num1 / num2
    insert_values(res)

window = tk.Tk()
window.title('MILITARY CALC')
window.geometry("300x300")
window.resizable(False, False)

operations = {'СУМ': (40, 150), 'ВЫЧ': (90, 150), 'УМН': (145, 150), 'ДЕЛ': (200, 150)}

for op, pos in operations.items():
    button = tk.Button(window, text=op, width=5, height=2, command=lambda op=op: calculate(op))
    button.place(x=pos[0], y=pos[1])

# окна ввода
number1_entry = tk.Entry(window, width=29)
number1_entry.place(x=55, y=50)
number2_entry = tk.Entry(window, width=29)
number2_entry.place(x=55, y=110)
answer_entry = tk.Entry(window, width=29)
answer_entry.place(x=55, y=230)

number1 = tk.Label(window, text='Введите первое число')
number1.place(x=75, y=25)
number2 = tk.Label(window, text='Введите второе число')
number2.place(x=75, y=85)
answer = tk.Label(window, text='ОТВЕТ')
answer.place(x=75, y=205)

window.mainloop()
