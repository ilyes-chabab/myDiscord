from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.resizable(False,False)


img = PhotoImage(file="C:\\Users\\b13im\\Downloads\\image (4).png")
Label(window, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(window, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

heading = Label(frame, text='Sign Up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

#####--------------------------------------------------------
def on_enter_user(e):
    user.delete(0, 'end')

def on_leave_user(e):
    if user.get() == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter_user)
user.bind("<FocusOut>", on_leave_user)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
#####--------------------------------------------------------

def on_enter_code(e):
    code.delete(0, 'end')

def on_leave_code(e):
    if code.get() == '':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter_code)
code.bind("<FocusOut>", on_leave_code)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

#####--------------------------------------------------------
def on_enter_confirm_code(e):
    confirm_code.delete(0, 'end')

def on_leave_confirm_code(e):
    if confirm_code.get() == '':
        confirm_code.insert(0, 'Confirm Password')

confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
confirm_code.place(x=30, y=200)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind("<FocusIn>", on_enter_confirm_code)
confirm_code.bind("<FocusOut>", on_leave_confirm_code)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=227)

#####--------------------------------------------------------

Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0,).place(x=35, y=280)
label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=90,y=340)

signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8')
signin.place(x=200,y=340)              
window.mainloop()
