import tkinter as tk
from tkinter import messagebox

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Page de Connexion")

        # Définition du style
        self.root.configure(bg='#f0f0f0')
        self.root.geometry('300x150')

        # Création des widgets avec un style amélioré
        self.label_username = tk.Label(root, text="Nom d'utilisateur:", bg='#f0f0f0', font=('Helvetica', 10))
        self.label_password = tk.Label(root, text="Mot de passe:", bg='#f0f0f0', font=('Helvetica', 10))
        self.entry_username = tk.Entry(root, font=('Helvetica', 10))
        self.entry_password = tk.Entry(root, show="*", font=('Helvetica', 10))
        self.button_login = tk.Button(root, text="Se connecter", command=self.login, bg='#4CAF50', fg='white', font=('Helvetica', 10))
        self.button_create_account = tk.Button(root, text="Créer un compte", command=self.create_account, bg='#2196F3', fg='white', font=('Helvetica', 10))

        # Placement des widgets
        self.label_username.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.label_password.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.entry_username.grid(row=0, column=1, padx=5, pady=5)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)
        self.button_login.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)
        self.button_create_account.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)

    def login(self):
        # Logique de connexion à implémenter ici
        messagebox.showinfo("Connexion", "Fonction de connexion non implémentée")

    def create_account(self):
        # Logique de création de compte à implémenter ici
        messagebox.showinfo("Créer un compte", "Fonction de création de compte non implémentée")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()
