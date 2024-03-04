from tkinter import *
from tkinter import messagebox
from User import *

window=Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.resizable(False,False)


# img = PhotoImage(file="C:\\Users\\b13im\\Downloads\\image (4).png")
# Label(window, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(window, width=350, height=430, bg='#fff')
frame.place(x=480, y=30)

heading = Label(frame, text='Sign Up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


#####--------------------------------------------------------

def sign_in():
    email_value = user.get()
    surname_value = surname.get()
    firstname_value = firstname.get()
    password_value = code.get()

    User.createUser(email_value, surname_value, firstname_value, password_value)

    user_id = User.get_user_id(email_value)
    
    User.Connection(user_id)



#####--------------------------------------------------------
def on_enter_user(e):
    user.delete(0, 'end')

def on_leave_user(e):
    if user.get() == '':
        user.insert(0, 'Email')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Email')
user.bind("<FocusIn>", on_enter_user)
user.bind("<FocusOut>", on_leave_user)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
#####--------------------------------------------------------

def on_enter_surname(e):
    surname.delete(0, 'end')

def on_leave_surname(e):
    if surname.get() == '':
        surname.insert(0, 'Surname')

surname = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
surname.place(x=30, y=130)
surname.insert(0, 'Surname')
surname.bind("<FocusIn>", on_enter_surname)
surname.bind("<FocusOut>", on_leave_surname)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=157)


######--------------------------------------------------------

def on_enter_firstname(e):
    firstname.delete(0, 'end')

def on_leave_firstname(e):
    if firstname.get() == '':
        firstname.insert(0, 'Firstname')

firstname = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
firstname.place(x=30, y=180)
firstname.insert(0, 'Firstname')
firstname.bind("<FocusIn>", on_enter_firstname)
firstname.bind("<FocusOut>", on_leave_firstname)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=207)

######--------------------------------------------------------

def on_enter_code(e):
    code.delete(0, 'end')

def on_leave_code(e):
    if code.get() == '':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=230)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter_code)
code.bind("<FocusOut>", on_leave_code)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=257)

#####--------------------------------------------------------

Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=sign_in).place(x=35, y=280)
label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=90,y=340)

signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8')
signin.place(x=200,y=340)              
window.mainloop()
