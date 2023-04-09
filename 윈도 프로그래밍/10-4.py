from tkinter import *
window = Tk()

photo = PhotoImage(file="C:/Users/user/PycharmProjects/pythonProject5/윈도 프로그래밍/dog.gif")
label1 = Label(window, image=photo)

label1.pack()

window.mainloop()
