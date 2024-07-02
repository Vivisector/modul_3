import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mult():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

window = tk.Tk()
window.title('CALC')
window.geometry("300x300")
window.resizable(False, False)
# кнопки действий
button_add = tk.Button(window, text="СУМ", width=5, height=2, command=add)
button_add.place(x=40, y=150)
button_sub = tk.Button(window, text="ВЫЧ", width=5, height=2, command=sub)
button_sub.place(x=90, y=150)
button_mult = tk.Button(window, text="УМН", width=5, height=2, command=mult)
button_mult.place(x=145, y=150)
button_div = tk.Button(window, text="ДЕЛ", width=5, height=2, command=div)
button_div.place(x=200, y=150)

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
