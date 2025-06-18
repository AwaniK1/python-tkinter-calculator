import tkinter as tk

calcu = ""

def add_to_calcu(symbol):
    global calcu
    calcu += str(symbol)
    result_text.delete(1.0, "end")
    result_text.insert(1.0, calcu)

def evaluate_calcu():
    global calcu
    try:
        
        result = str(eval(calcu))
        calcu = ""
        result_text.delete(1.0, "end")
        result_text.insert(1.0, result)
    except:
        clear_field()
        result_text.insert(1.0, "Error")


def clear_field():
    global calcu 
    result_text.delete(1.0, "end")

root = tk.Tk()
root.title("CALCULATOR")
root.geometry("300x275")

result_text = tk.Text(root, height=2, width=16, font=("Arial",24))
result_text.grid(columnspan=5)

btn1 = tk.Button(root, text="1", command=lambda: add_to_calcu(1), width=5, font=("Arial",14))
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text="2", command=lambda: add_to_calcu(2), width=5, font=("Arial",14))
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text="3", command=lambda: add_to_calcu(3), width=5, font=("Arial",14))
btn3.grid(row=2, column=3)
btn4 = tk.Button(root, text="4", command=lambda: add_to_calcu(4), width=5, font=("Arial",14))
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command=lambda: add_to_calcu(5), width=5, font=("Arial",14))
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command=lambda: add_to_calcu(6), width=5, font=("Arial",14))
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command=lambda: add_to_calcu(7), width=5, font=("Arial",14))
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text="8", command=lambda: add_to_calcu(8), width=5, font=("Arial",14))
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text="9", command=lambda: add_to_calcu(9), width=5, font=("Arial",14))
btn9.grid(row=4, column=3)
btn0 = tk.Button(root, text="0", command=lambda: add_to_calcu(0), width=5, font=("Arial",14))
btn0.grid(row=5, column=2)
btnplus = tk.Button(root, text="+", command=lambda: add_to_calcu("+"), width=5, font=("Arial",14))
btnplus.grid(row=2, column=4)
btnminus = tk.Button(root, text="-", command=lambda: add_to_calcu("-"), width=5, font=("Arial",14))
btnminus.grid(row=3, column=4)
btnmul = tk.Button(root, text="*", command=lambda: add_to_calcu("*"), width=5, font=("Arial",14))
btnmul.grid(row=4, column=4)
btndiv = tk.Button(root, text="/", command=lambda: add_to_calcu("/"), width=5, font=("Arial",14))
btndiv.grid(row=5, column=4)
btnopen = tk.Button(root, text="(", command=lambda: add_to_calcu("("), width=5, font=("Arial",14))
btnopen.grid(row=5, column=1)
btnclose = tk.Button(root, text=")", command=lambda: add_to_calcu(")"), width=5, font=("Arial",14))
btnclose.grid(row=5, column=3)
btnclear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial",14))
btnclear.grid(row=6, column=1, columnspan=2)
btnequal = tk.Button(root, text="=", command=evaluate_calcu, width=11, font=("Arial",14))
btnequal.grid(row=6, column=3, columnspan=2)

root.mainloop()