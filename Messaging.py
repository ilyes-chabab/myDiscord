import tkinter as tk
from tkinter import ttk
import mysql.connector

class Messaging:
    def __init__(self):
        root = tk.Tk()
        self.root = root
        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ('id_user_emeteur','heure', 'message')

        # Connectez-vous à votre base de données MySQL
        self.connection = mysql.connector.connect(
            host='ilyes-chabab.students-laplateforme.io',
            user='ilyes-chabab',
            password='Nitrate13140',
            database='ilyes-chabab_myDiscord',
        )
        self.cursor = self.connection.cursor()

        # Configurez les colonnes dans Treeview
    
        self.tree.column('id_user_emeteur', anchor='center', width=50)  # Ajustez la largeur selon vos besoins
        self.tree.column('heure', anchor='center', width=150)
        self.tree.column('message', anchor='w', width=500)  # 'w' signifie alignement à gauche (left)

        # Remplissez le Treeview avec les données
        self.fetch_data()

        # Ajoutez le Treeview à la fenêtre principale
        self.tree.pack(expand=True, fill='both')

    def fetch_data(self):
        # Sélectionnez les colonnes 'heure_d_envoie' et 'message' de la table
        self.cursor.execute(f"SELECT user.surname , message.heure, message.message FROM message inner join user on message.id_user_emeteur=user.id")
        rows = self.cursor.fetchall()

        # Effacez le contenu actuel du Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ajoutez les nouvelles données au Treeview
        for row in rows:
            self.tree.insert('', 'end', values=row)


message=Messaging()
message.root.mainloop()

