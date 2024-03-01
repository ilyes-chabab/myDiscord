from tkinter import *
from tkinter import messagebox
from User import *


# Permet de définir la fenêtre et ses caractéristiques

root=Tk()
root.title('Login')
root.geometry('925x550+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

# Fonction qui s'appelle lorsqu'on clique sur le bouton sign in et qui permet l'accès à la page principale

def signin():
    # Variable qui récupère l'email et le mdp entré par l'user
    username = user.get()
    password = code.get()
    
    # Vérifie que l'email et le password sont bien présent dans la table user et ouvre une fenêtre
    if User.checkForAccount(username) == True and password == User.checkForPassword(username):
         screen=Toplevel(root)
         screen.title("App")
         screen.geometry('925x500+300+200')
         screen.config(bg="white")
         
         Label(screen,text='Hello Everyone!',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)

         screen.mainloop()

    # Message d'erreur lorsque l'email et le mdp sont invalide
    elif username != User.checkForAccount(username) and password != User.checkForPassword(username):
         messagebox.showerror('Invalid', 'Invalid email and password')
    
    # Message d'erreur lorsque le mdp est invalide

    elif password != User.checkForPassword(username):
        messagebox.showerror('Invalid', 'Invalid password')

    # Message d'erreur lorsque l'email est invalide
        
    elif username != User.checkForAccount(username):
        messagebox.showerror('Invalid', 'Invalid email')


Label(root,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8' ,bg='white' ,font=('Microsoft YaHei UI Light',23, 'bold'))
heading.place(x=100,y=5)

#########----------------------------------------------------------
# Vide le contenu de la zone de texte de l'email

def on_enter(e):
    user.delete(0, 'end')

# Rempli la zone de texte de l'email avec le mot 'Email'
    
def on_leave(e):
    name = user.get()
    if name =='':
        user.insert(0, 'Email')


# Créer la zone de texte pour l'email   
             
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light', 11))
user.place(x=30,y=80)
user.insert(0,'Email')

# Supprime le contenu de la zone de texte quand on clique à l'intérieur

user.bind('<FocusIn>',on_enter)

# Rempli de nouveau la zone de texte lorsqu'on quitte cette dernière

user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#########----------------------------------------------------------

# Vide le contenu de la zone de texte du mdp

def on_enter(e):
    code.delete(0, 'end')

# Rempli la zone de texte du mdp avec le mot 'Password'

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

# Créer la zone de texte pour le mdp  

code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light', 11))
code.place(x=30,y=150)
code.insert(0,'Password')

# Supprime le contenu de la zone de texte quand on clique à l'intérieur

code.bind('<FocusIn>',on_enter)

# Rempli de nouveau la zone de texte lorsqu'on quitte cette dernière

code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

###############################################################

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8' ,fg='white',border=0, command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?" ,fg='black' ,bg='white',font=('Microsoft YaHei UI Light' ,9))
label.place(x=75,y=270)    

sign_up= Button(frame,width=6,text='Sign up' ,border=0 ,bg='white' ,cursor='hand2' ,fg='#57a1f8')
sign_up.place(x=215,y=270)

root.mainloop()