from tkinter import *
root = Tk()
root.title("Calculator by Raghu")
e = Entry(root,  width=40, borderwidth=5)
e.grid(row=0, column=0, rowspan=1,columnspan=4,pady=15)


def button_click(number):
    current = e.get()
        
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global f_num
    global math
    math='addition'
    f_num=int(first_number)
    e.delete(0,END)

def button_sub():
    first_number=e.get()
    global f_num
    global math
    math='subtraction'
    f_num=int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math='multiplication'
    f_num=int(first_number)
    e.delete(0,END)

def button_divide():
    first_number=e.get()
    global f_num
    global math
    math='division'
    f_num=int(first_number)
    e.delete(0,END)

def button_percent():
    first_number=e.get()
    global f_num
    global math
    math='percent'
    f_num=int(first_number)

def button_square():
    first_number=e.get()
    global f_num
    global math
    math='square'
    f_num=int(first_number)
def button_cube():
    first_number=e.get()
    global f_num
    global math
    math='cube'
    f_num=int(first_number)

def button_squareroot():
    first_number=e.get()
    global f_num
    global math
    math='squareroot'
    f_num=int(first_number)


def button_equal():
    second_number=e.get()
    e.delete(0,END)

    if math=='addition':
        e.insert(0,f_num+int(second_number))
    
    elif math=='subtraction':
        e.insert(0,f_num-int(second_number))
    
    elif math=='multiplication':
        e.insert(0,f_num*int(second_number))
    
    elif math=='division':
        e.insert(0,f_num/int(second_number))
    
    elif math=='percent':
        e.insert(0,f_num/100)
    elif math=='square':
        e.insert(0,f_num**2)
    
    elif math=='cube':
        e.insert(0,f_num**3)
    
    elif math=='squareroot':
        e.insert(0,f_num**0.5)

    






button_1 = Button(root, text="1", padx=30, pady=10,
                  command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=10,
                  command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=10,
                  command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=10,
                  command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=10,
                  command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=10,
                  command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=10,
                  command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=10,
                  command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=10,
                  command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=10,
                  command=lambda: button_click(0))
button_add = Button(root, text="+", padx=30, pady=10,command=button_add)
button_sub = Button(root, text="-", padx=30, pady=10,command=button_sub)
button_multiply = Button(root, text="*", padx=30, pady=10,command=button_multiply)
button_divide = Button(root, text="/", padx=30, pady=10,command=button_divide)
button_percent = Button(root, text="%", padx=28, pady=10,command=button_percent)
button_square = Button(root, text="x^2", padx=23, pady=10,command=button_square)
button_cube = Button(root, text="x^3", padx=23, pady=10,command=button_cube)
button_squareroot = Button(root, text="√", padx=29, pady=10,command=button_squareroot)
button_clear = Button(root, text="C", padx=28, pady=10,command=button_clear,
                      bg="#009FAA", fg="white")
button_equals = Button(root, text="=", padx=30, pady=10,
                       bg="#009FAA", fg="white",command=button_equal)
button_decimal=Button(root,text=".",padx=30.95,pady=10,command=lambda: button_click('.'))

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_add.grid(row=5, column=3)
button_sub.grid(row=4, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=2, column=3)
button_equals.grid(row=6, column=3)
button_0.grid(row=6, column=1)
button_decimal.grid(row=6,column=2)

button_percent.grid(row=1, column=0)
button_square.grid(row=2, column=1)
button_cube.grid(row=2, column=2)
button_squareroot.grid(row=2, column=0)
button_clear.grid(row=1, column=3)
root.mainloop()
