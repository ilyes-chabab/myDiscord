import tkinter as tk
import re
import subprocess
from tkinter import messagebox
from User import *

class LoginApp:
    def __init__(self, master):
        # Initialisation de l'application avec la fenêtre principale comme maître
        self.master = master
        master.title('Login')  # Titre de la fenêtre
        master.geometry('925x550+300+200')  # Taille et position de la fenêtre
        master.configure(bg="#fff")  # Couleur de fond de la fenêtre
        master.resizable(False, False)  # Empêcher le redimensionnement de la fenêtre

        # Création d'un espace vide en haut de la fenêtre
        tk.Label(master, bg='white').place(x=50, y=50)

        # Création d'un cadre pour contenir les éléments de la fenêtre
        self.frame = tk.Frame(master, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)

        # Titre "Sign in"
        self.heading = tk.Label(self.frame, text='Sign in', fg='#57a1f8', bg='white',
                             font=('Microsoft YaHei UI Light', 23, 'bold'))
        self.heading.place(x=100, y=5)

        # Champ de saisie pour l'email
        self.user = tk.Entry(self.frame, width=25, fg='black', border=0, bg="white",
                          font=('Microsoft YaHei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Email')
        self.user.bind('<FocusIn>', self.on_enter)  # Gestion de l'événement "FocusIn"
        self.user.bind('<FocusOut>', self.on_leave)  # Gestion de l'événement "FocusOut"

        # Ligne de séparation
        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        # Champ de saisie pour le mot de passe
        self.code = tk.Entry(self.frame, width=25, fg='black', border=0, bg="white",
                          font=('Microsoft YaHei UI Light', 11))
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Password')
        self.code.bind('<FocusIn>', self.on_enter)  # Gestion de l'événement "FocusIn"
        self.code.bind('<FocusOut>', self.on_leave)  # Gestion de l'événement "FocusOut"

        # Ligne de séparation
        tk.Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        # Bouton "Sign in"
        tk.Button(self.frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0,
               command=lambda:[self.sign_in(),self.return_id()]).place(x=35, y=204)

        # Texte "Don't have an account?"
        tk.Label(self.frame, text="Don't have an account?", fg='black', bg='white',
              font=('Microsoft YaHei UI Light', 9)).place(x=75, y=270)

        # Bouton "Sign up"
        tk.Button(self.frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8',
               command=self.open_signup).place(x=215, y=270)

    # Méthode appelée lorsqu'on entre dans un champ de saisie
    def on_enter(self, e):
        widget = e.widget
        widget.delete(0, 'end')  # Supprime le texte existant dans le champ de saisie

    # Méthode appelée lorsqu'on quitte un champ de saisie
    def on_leave(self, e):
        widget = e.widget
        if widget.get() == '':  # Si le champ de saisie est vide
            if widget == self.user:  # Si c'est le champ de l'email
                widget.insert(0, 'Email')  # Remplir avec "Email"
            else:  # Sinon (champ du mot de passe)
                widget.insert(0, 'Password')  # Remplir avec "Password"

    # Méthode pour gérer la connexion
    def sign_in(self):
        username = self.user.get()
        password = self.code.get()

        # Vérification des informations d'identification

        if User.checkForAccount(username) and password == User.checkForPassword(username):
            user_id = User.get_user_id(username)
            self.master.withdraw()  # Masquer la fenêtre de connexion
            self.open_app_screen()  # Ouvrir l'écran d'application avec l'ID de l'utilisateur
        
        elif self.is_valid_email(username) == False:
            messagebox.showerror('Invalid', 'Please enter a valid email')
        
        elif username != User.checkForAccount(username) and password != User.checkForPassword(username):
            messagebox.showerror('Invalid', 'Invalid email and password')

        elif password != User.checkForPassword(username):
            messagebox.showerror('Invalid', 'Invalid password')

        elif username != User.checkForAccount(username):
            messagebox.showerror('Invalid', 'Invalid email')


    
    # Fonction pour retourner l'ID de l'utilisateur
    def return_id(self):
        email_value = self.user.get()
        user_id = User.get_user_id(email_value)
        return user_id

    def is_valid_email(self ,email_value):
        # Modèle d'expression régulière pour valider l'adresse e-mail
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # Vérification de l'adresse e-mail avec l'expression régulière
        if re.match(pattern, email_value):
            return True
        else:
            return False

    # Méthode pour ouvrir l'écran d'inscription
    def open_signup(self):
        self.master.withdraw()  # Masquer la fenêtre de connexion
        signup_screen = tk.Toplevel(self.master)  # Créer une nouvelle fenêtre pour l'inscription
        signup_app = SignUpApp(signup_screen)  # Initialiser l'application d'inscription
        signup_screen.protocol("WM_DELETE_WINDOW", lambda: self.on_close_signup(signup_screen))  # Définir une action lorsque la fenêtre est fermée

    # Méthode pour ouvrir l'écran d'application après la connexion
    def open_app_screen(self):
        # Remplacez 'chemin/vers/votre/programme.py' par le chemin de votre fichier de messagerie
        chemin_programme_messagerie = 'Main-page.py'
        
        # Utilisez subprocess pour exécuter le programme de messagerie
        subprocess.Popen(['python', chemin_programme_messagerie])

    # Méthode appelée lorsque la fenêtre d'inscription est fermée
    def on_close_signup(self, signup_screen):
        self.master.deiconify()  # Réafficher la fenêtre de connexion lorsque la fenêtre d'inscription est fermée
        signup_screen.destroy()  # Détruire la fenêtre d'inscription pour libérer les ressources

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
        self.sign_up_button = tk.Button(self.frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=lambda:[self.sign_up(),self.return_id_2()])
        self.sign_up_button.place(x=35, y=280)

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
    def sign_up(self):
        email_value = self.user.get()
        surname_value = self.surname.get()
        firstname_value = self.firstname.get()
        password_value = self.code.get()

        if User.checkForAccount(email_value):
            messagebox.showerror('Invalid', 'Your email is already associed to an account')

        elif self.is_valid_email(email_value) == False:
            messagebox.showerror('Invalid', 'Please enter a valid email')

        else:
            User.createUser(email_value, surname_value, firstname_value, password_value)
            self.master.withdraw()  # Masquer la fenêtre de connexion
            self.open_app_screen()

    # Fonction pour retourner l'ID de l'utilisateur
    def return_id_2(self):
        email_value = self.user.get()
        user_id = User.get_user_id(email_value)
        return user_id

    def is_valid_email(self ,email_value):
        # Modèle d'expression régulière pour valider l'adresse e-mail
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # Vérification de l'adresse e-mail avec l'expression régulière
        if re.match(pattern, email_value):
            return True
        else:
            return False
    
    def open_app_screen(self):
        self.master.destroy()
        # Remplacez 'chemin/vers/votre/programme.py' par le chemin de votre fichier de messagerie
        chemin_programme_messagerie = 'Main-page.py'
        
        # Utilisez subprocess pour exécuter le programme de messagerie
        subprocess.Popen(['python', chemin_programme_messagerie])
    
    # Fonction pour ouvrir l'écran de connexion
    def open_login(self):
        self.master.destroy()  # Fermer la fenêtre d'inscription
        login_screen = tk.Tk()  # Créer une nouvelle fenêtre de connexion
        login_app = LoginApp(login_screen)  # Initialiser l'application de connexion
        login_screen.mainloop()  # Lancer l'application de connexion

# Création de la fenêtre principale et lancement de l'application de connexion
root = tk.Tk()
app = LoginApp(root)
root.mainloop()