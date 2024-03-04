from tkinter import *
from tkinter import messagebox
from User import *

# Initialisation de la fenêtre principale
window=Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.resizable(False,False)

# img = PhotoImage(file="C:\\Users\\b13im\\Downloads\\image (4).png")
# Label(window, image=img, border=0, bg='white').place(x=50, y=90)


# Création d'un cadre pour contenir les éléments de la fenêtre
frame = Frame(window, width=350, height=430, bg='#fff')
frame.place(x=480, y=30)

# Ajout d'un titre à la fenêtre
heading = Label(frame, text='Sign Up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Fonction pour gérer la soumission du formulaire d'inscription
def sign_in():
    # Permet de récupérer et d'utiliser les informations saisies par l'utilisateur
    email_value = user.get()
    surname_value = surname.get()
    firstname_value = firstname.get()
    password_value = code.get()

    # Vérifie si l'utilisateur n'a pas déja crée un compte grâce à son adresse mail
    if User.checkForAccount(email_value) == True:
        messagebox.showerror('Invalid', 'Your email is already associed to an account')
    else:
        # Sinon ,création d'un nouvel utilisateur dans la bdd avec les informations saisies
        User.createUser(email_value, surname_value, firstname_value, password_value)

    # Récupération de l'ID de l'utilisateur créé
    user_id = User.get_user_id(email_value)
    
    # Changement de la valeur 'state' de l'utilisateur pour le rendre 'online'
    User.Connection(user_id)

# Fonctions pour gérer les événements de focus sur les champs de saisie
def on_enter_user(e):
    user.delete(0, 'end')

def on_leave_user(e):
    if user.get() == '':
        user.insert(0, 'Email')

# Création du champ de saisie pour l'email
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Email')
user.bind("<FocusIn>", on_enter_user)
user.bind("<FocusOut>", on_leave_user)

# Création d'une séparation visuelle entre les champs de saisie
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# Fonctions pour gérer les événements de focus sur le champ de saisie du nom de famille
def on_enter_surname(e):
    surname.delete(0, 'end')

def on_leave_surname(e):
    if surname.get() == '':
        surname.insert(0, 'Surname')

# Création du champ de saisie pour le nom de famille
surname = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
surname.place(x=30, y=130)
surname.insert(0, 'Surname')
surname.bind("<FocusIn>", on_enter_surname)
surname.bind("<FocusOut>", on_leave_surname)

# Création d'une séparation visuelle entre les champs de saisie
Frame(frame, width=295, height=2, bg='black').place(x=25, y=157)

# Fonctions pour gérer les événements de focus sur le champ de saisie du prénom
def on_enter_firstname(e):
    firstname.delete(0, 'end')

def on_leave_firstname(e):
    if firstname.get() == '':
        firstname.insert(0, 'Firstname')

# Création du champ de saisie pour le prénom
firstname = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
firstname.place(x=30, y=180)
firstname.insert(0, 'Firstname')
firstname.bind("<FocusIn>", on_enter_firstname)
firstname.bind("<FocusOut>", on_leave_firstname)

# Création d'une séparation visuelle entre les champs de saisie
Frame(frame, width=295, height=2, bg='black').place(x=25, y=207)

# Fonctions pour gérer les événements de focus sur le champ de saisie du mot de passe
def on_enter_code(e):
    code.delete(0, 'end')

def on_leave_code(e):
    if code.get() == '':
        code.insert(0, 'Password')

# Création du champ de saisie pour le mot de passe
code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=230)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter_code)
code.bind("<FocusOut>", on_leave_code)

# Création d'une séparation visuelle entre les champs de saisie
Frame(frame, width=295, height=2, bg='black').place(x=25, y=257)

# Création du bouton pour soumettre le formulaire d'inscription
Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=sign_in).place(x=35, y=280)

# Création d'un label pour indiquer la possibilité de se connecter si déjà inscrit
label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=90,y=340)

# Création d'un bouton pour se connecter si déjà inscrit
signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8')
signin.place(x=200,y=340)              

# Lancement de la boucle principale de l'application
window.mainloop()
