from tkinter import *
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
        Label(master, bg='white').place(x=50, y=50)

        # Création d'un cadre pour contenir les éléments de la fenêtre
        self.frame = Frame(master, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)

        # Titre "Sign in"
        self.heading = Label(self.frame, text='Sign in', fg='#57a1f8', bg='white',
                             font=('Microsoft YaHei UI Light', 23, 'bold'))
        self.heading.place(x=100, y=5)

        # Champ de saisie pour l'email
        self.user = Entry(self.frame, width=25, fg='black', border=0, bg="white",
                          font=('Microsoft YaHei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Email')
        self.user.bind('<FocusIn>', self.on_enter)  # Gestion de l'événement "FocusIn"
        self.user.bind('<FocusOut>', self.on_leave)  # Gestion de l'événement "FocusOut"

        # Ligne de séparation
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        # Champ de saisie pour le mot de passe
        self.code = Entry(self.frame, width=25, fg='black', border=0, bg="white",
                          font=('Microsoft YaHei UI Light', 11))
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Password')
        self.code.bind('<FocusIn>', self.on_enter)  # Gestion de l'événement "FocusIn"
        self.code.bind('<FocusOut>', self.on_leave)  # Gestion de l'événement "FocusOut"

        # Ligne de séparation
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        # Bouton "Sign in"
        Button(self.frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0,
               command=self.signin).place(x=35, y=204)

        # Texte "Don't have an account?"
        Label(self.frame, text="Don't have an account?", fg='black', bg='white',
              font=('Microsoft YaHei UI Light', 9)).place(x=75, y=270)

        # Bouton "Sign up"
        Button(self.frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8').place(x=215,
                                                                                                                y=270)

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
    def signin(self):
        username = self.user.get()
        password = self.code.get()

        # Vérification des informations d'identification
        if User.checkForAccount(username) and password == User.checkForPassword(username):
            user_id = User.get_user_id(username)
            screen = Toplevel(self.master)
            screen.title("App")
            screen.geometry('925x500+300+200')
            screen.config(bg="white")
            Label(screen, text='Hello Everyone!', bg='#fff', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

        elif username != User.checkForAccount(username) and password != User.checkForPassword(username):
            messagebox.showerror('Invalid', 'Invalid email and password')

        elif password != User.checkForPassword(username):
            messagebox.showerror('Invalid', 'Invalid password')

        elif username != User.checkForAccount(username):
            messagebox.showerror('Invalid', 'Invalid email')

# Création de la fenêtre principale et lancement de l'application
root = Tk()
app = LoginApp(root)
root.mainloop()