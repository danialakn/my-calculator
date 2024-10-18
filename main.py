import math
import tkinter
from tkinter import *

window = tkinter.Tk()
window.title('Calculator')
window.geometry("400x400")

# ایجاد فیلدهای ورودی در ابتدا
field1 = tkinter.Entry(window)
field2 = tkinter.Entry(window)

# ایجاد برچسب نتیجه
result_label = Label(window, text="Result: ")


def calculate():
    try:
        num1 = float(field1.get())
        operation = v.get()

        if operation in ["1", "2", "3", "4"]:
            num2 = float(field2.get())  # گرفتن مقدار فیلد دوم برای عملیات دوتایی
            if operation == "1":  # جمع
                result = num1 + num2
            elif operation == "2":  # تفریق
                result = num1 - num2
            elif operation == "3":  # ضرب
                result = num1 * num2
            elif operation == "4":  # تقسیم
                result = num1 / num2 if num2 != 0 else "Cannot divide by zero!"
        elif operation == "5":  # توان
            result = num1 ** 2
        elif operation == "6":  # جذر
            result = math.sqrt(num1)

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Please enter valid numbers!")


# تابع برای مدیریت تغییر فیلدهای ورودی بر اساس انتخاب عملیات
def func():
    operation = v.get()

    # حذف فیلدهای ورودی قبلی
    field1.grid_forget()
    field2.grid_forget()

    # برای توان و جذر فقط یک فیلد ورودی نمایش داده می‌شود
    if operation == "5" or operation == "6":
        field1.grid(row=1, column=1, pady=10)  # نشان دادن فقط فیلد 1
    else:
        field1.grid(row=1, column=1, pady=10)  # نشان دادن فیلد 1
        field2.grid(row=1, column=2, pady=10)  # نشان دادن فیلد 2


label1 = Label(window, text="Choose what you want to do")
label1.grid(row=0, column=1, pady=10)

# متغیر برای رادیوباتن‌ها
v = StringVar(window, "1")

# ایجاد رادیوباتن‌ها
values = {"sum": "1",
          "subtraction": "2",
          "multiplication": "3",
          "division": "4",
          "square": "5",
          "root": "6"}

row_index = 2
for (text, value) in values.items():
    Radiobutton(window, text=text, variable=v,
                value=value, background="light blue", indicator=0, command=func).grid(row=row_index, column=1,
                                                                                      sticky="w", pady=5)
    row_index += 1

# دکمه محاسبه
calculate_button = Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=row_index, column=1, pady=10)

# نمایش برچسب نتیجه
result_label.grid(row=row_index + 1, column=1, pady=10)

window.mainloop()

