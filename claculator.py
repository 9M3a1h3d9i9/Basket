from tkinter import *

#__________________( functions )________________


def next():
    pass

def click_1():
    
    int_a.set(int_input.get())
    # print(int_input.get())
    int_b = int_a.set(int_input.get())
    # list_1 = list(int_a)
    print(int_b)

#___________________( setting )_________________
window = Tk()
window.geometry("400x600")
window.title("Calculator")
window.resizable(width=False,height=False)

# color back ground
color = "black"
window.configure(bg=color)

#___________________( text variable )___________

int_a = IntVar()
int_b = IntVar()
int_finall = IntVar()


#___________________( frames )__________________
top_first = Frame(window,width=400,height=60,bg="white")
top_first.pack(side=TOP)

top_second = Frame(window,width=400,height=60,bg="gray")
top_second.pack(side=TOP)

top_third = Frame(window,width=400,height=60,bg="blue")
top_third.pack(side=TOP)

top_forth = Frame(window,width=400,height=60,bg="red")
top_forth.pack(side=TOP)

#___________________( button )___________________

button_1 = Button(window,text="=",command=lambda : click_1())
button_1.place(x=350,y=550)



#___________________( label )____________________

label_0 = Label(window, text="calculating")
label_0.place(x=0,y=0)

# Entry
int_input = Entry(window)
int_input.place(x=140,y=75)

label_1 = Label(window,textvariable = int_a ) 
label_1.place(x=140,y=30)

window.mainloop()