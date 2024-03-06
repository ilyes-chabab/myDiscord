import tkinter as tk
from tkinter import messagebox
from User import *
from Signin import LoginApp

class SignUpApp:
    def __init__(self, master):
        # Initialisation de l'application avec la fenêtre principale comme maître
        self.master = master
        master.title("SignUp")  # Titre de la fenêtre
        master.geometry('925x500+300+200')  # Taille et position de la fenêtre
        master.resizable(False,False)  # Empêcher le redimensionnement de la fenêtre

        # Création d'un cadre pour contenir les éléments de la fenêtre
        self.frame = tk.Frame(master, width=350, height=430, bg='#fff')
        self.frame.place(x=480, y=30)

        # Ajout d'un titre à l'application
        self.heading = tk.Label(self.frame, text='Sign Up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
        self.heading.place(x=100, y=5)

        # Champ de saisie pour l'email
        self.user = tk.Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Email')
        self.user.bind("<FocusIn>", self.on_enter_user)
        self.user.bind("<FocusOut>", self.on_leave_user)

        # Ligne de séparation
        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        # Champ de saisie pour le nom de famille
        self.surname = tk.Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        self.surname.place(x=30, y=130)
        self.surname.insert(0, 'Surname')
        self.surname.bind("<FocusIn>", self.on_enter_surname)
        self.surname.bind("<FocusOut>", self.on_leave_surname)

        # Ligne de séparation
        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=157)

        # Champ de saisie pour le prénom
        self.firstname = tk.Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        self.firstname.place(x=30, y=180)
        self.firstname.insert(0, 'Firstname')
        self.firstname.bind("<FocusIn>", self.on_enter_firstname)
        self.firstname.bind("<FocusOut>", self.on_leave_firstname)

        # Ligne de séparation
        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=207)

        # Champ de saisie pour le mot de passe
        self.code = tk.Entry(self.frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        self.code.place(x=30, y=230)
        self.code.insert(0, 'Password')
        self.code.bind("<FocusIn>", self.on_enter_code)
        self.code.bind("<FocusOut>", self.on_leave_code)

        # Ligne de séparation
        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=257)

        # Bouton pour soumettre le formulaire d'inscription
        self.sign_in_button = tk.Button(self.frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=self.sign_in)
        self.sign_in_button.place(x=35, y=280)

        # Label pour indiquer la possibilité de se connecter si déjà inscrit
        self.label = tk.Label(self.frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light',9))
        self.label.place(x=90, y=340)

        # Bouton pour se connecter si déjà inscrit
        self.signin = tk.Button(self.frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=self.open_login)
        self.signin.place(x=200, y=340)

    # Fonctions pour gérer les événements de focus sur les champs de saisie
    def on_enter_user(self, e):
        self.user.delete(0, 'end')

    def on_leave_user(self, e):
        if self.user.get() == '':
            self.user.insert(0, 'Email')

    def on_enter_surname(self, e):
        self.surname.delete(0, 'end')

    def on_leave_surname(self, e):
        if self.surname.get() == '':
            self.surname.insert(0, 'Surname')

    def on_enter_firstname(self, e):
        self.firstname.delete(0, 'end')

    def on_leave_firstname(self, e):
        if self.firstname.get() == '':
            self.firstname.insert(0, 'Firstname')

    def on_enter_code(self, e):
        self.code.delete(0, 'end')

    def on_leave_code(self, e):
        if self.code.get() == '':
            self.code.insert(0, 'Password')

    # Fonction pour gérer la soumission du formulaire d'inscription
    def sign_in(self):
        email_value = self.user.get()
        surname_value = self.surname.get()
        firstname_value = self.firstname.get()
        password_value = self.code.get()

        if User.checkForAccount(email_value):
            messagebox.showerror('Invalid', 'Your email is already associed to an account')
        else:
            User.createUser(email_value, surname_value, firstname_value, password_value)

    # Fonction pour retourner l'ID de l'utilisateur
    def return_id(self):
        email_value = self.user.get()
        user_id = User.get_user_id(email_value)
        return user_id

    # Fonction pour ouvrir l'écran de connexion
    def open_login(self):
        self.master.destroy()  # Fermer la fenêtre d'inscription
        login_screen = tk.Tk()  # Créer une nouvelle fenêtre de connexion
        login_app = LoginApp(login_screen)  # Initialiser l'application de connexion
        login_screen.mainloop()  # Lancer l'application de connexion
