
from tkinter import *

window = Tk()
window.geometry("315x510")
window.resizable(False, False)
window.title("Calculator")
window.iconbitmap("calculator.ico")
window.configure(bg="black")

text1 = Label(window,
              text="Standart",
              font=("Arial", 20, "bold"),
              fg="purple",
              bg="black")
text1.pack(anchor="w", padx=20, pady=10)

entry = Entry(window,
              width=15,
              font=("Arial", 25, "bold"),
              justify="right")
entry.pack(anchor="w", padx=10, pady=10)



def add_number(number):
    entry.insert(END, number)


def clear():
    entry.delete(0, END)


def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current[:-1])


def calculator():
    expression = entry.get()

    try:
        if not expression or any(
            char not in "0123456789+-*/. " for char in expression
        ):
            raise ValueError

        result = eval(expression, {"__builtins__": None}, {})

        entry.delete(0, END)
        entry.insert(END, str(result))

    except (SyntaxError, TypeError, ZeroDivisionError, ValueError):
        entry.delete(0, END)
        entry.insert(END, "Error")


def change_sign():
    current = entry.get()

    if current:
        if current.startswith("-"):
            entry.delete(0, 1)
        else:
            entry.insert(0, "-")



btn_clear = Button(window, text="CLEAR", width=11, height=2,
                   bg="purple", fg="gold",
                   command=clear)
btn_clear.place(x=10, y=120)

btn_back = Button(window, text="⌫", width=5, height=2,
                  bg="gold", command=backspace)
btn_back.place(x=150, y=120)

btn_div = Button(window, text="÷", width=5, height=2,
                 bg="gold", command=lambda: add_number("/"))
btn_div.place(x=230, y=120)

btn7 = Button(window, text="7", width=5, height=2,
              bg="gold", command=lambda: add_number("7"))
btn7.place(x=10, y=185)

btn8 = Button(window, text="8", width=5, height=2,
              bg="gold", command=lambda: add_number("8"))
btn8.place(x=85, y=185)

btn9 = Button(window, text="9", width=5, height=2,
              bg="gold", command=lambda: add_number("9"))
btn9.place(x=160, y=185)

btn_mul = Button(window, text="×", width=5, height=2,
                 bg="gold", command=lambda: add_number("*"))
btn_mul.place(x=235, y=185)

btn4 = Button(window, text="4", width=5, height=2,
              bg="gold", command=lambda: add_number("4"))
btn4.place(x=10, y=250)

btn5 = Button(window, text="5", width=5, height=2,
              bg="gold", command=lambda: add_number("5"))
btn5.place(x=85, y=250)

btn6 = Button(window, text="6", width=5, height=2,
              bg="gold", command=lambda: add_number("6"))
btn6.place(x=160, y=250)

btn_minus = Button(window, text="-", width=5, height=2,
                   bg="gold", command=lambda: add_number("-"))
btn_minus.place(x=235, y=250)

btn1 = Button(window, text="1", width=5, height=2,
              bg="gold", command=lambda: add_number("1"))
btn1.place(x=10, y=315)

btn2 = Button(window, text="2", width=5, height=2,
              bg="gold", command=lambda: add_number("2"))
btn2.place(x=85, y=315)

btn3 = Button(window, text="3", width=5, height=2,
              bg="gold", command=lambda: add_number("3"))
btn3.place(x=160, y=315)

btn_plus = Button(window, text="+", width=5, height=2,
                  bg="gold", command=lambda: add_number("+"))
btn_plus.place(x=235, y=315)



btn_sign = Button(window, text="+/-", width=5, height=2,
                  bg="gold", command=change_sign)
btn_sign.place(x=10, y=380)

btn0 = Button(window, text="0", width=5, height=2,
              bg="gold", command=lambda: add_number("0"))
btn0.place(x=85, y=380)

btn_dot = Button(window, text=".", width=5, height=2,
                 bg="gold", command=lambda: add_number("."))
btn_dot.place(x=160, y=380)

btn_equal = Button(window, text="=", width=5, height=2,
                   bg="purple", fg="gold",
                   command=calculator)
btn_equal.place(x=235, y=380)


window.mainloop()
