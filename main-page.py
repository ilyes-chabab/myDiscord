from tkinter import *
from tkinter import ttk
import tkinter as tk
from channel import Channel
from db import Db
from Message import Message
import time

class main_page:
    
    def __init__(self):
        # Création de la fenêtre principale
        self.db=Db('ilyes-chabab.students-laplateforme.io','ilyes-chabab','Nitrate13140','ilyes-chabab_myDiscord')
        self.channel=Channel()
        self.root = tk.Tk()
        self.root.title('main-page') 
        self.id_user=2
        self.id_channel=0
        self.number_channel=self.channel.numberChannelForUser(self.id_user)[self.id_channel][0]
        self.name_channel=self.channel.getNameChannel(self.number_channel)
        self.tree = ttk.Treeview(self.root, columns= ('id_user_emeteur','heure', 'message'))
        
        self.tree.place(x=333, y=0)
        self.messaging()

    def messaging(self):
        print("jqshd")
        self.tree.column('id_user_emeteur', anchor='center', width=50)  # Ajustez la largeur 
        self.tree.column('heure', anchor='center', width=150)
        self.tree.column('message', anchor='w', width=400)  # 'w' signifie west : alignement à gauche (left)
        # Remplissez le Treeview avec les données
        self.fetch_data(self.number_channel)
        # Ajoutez le Treeview à la fenêtre principale
        self.tree.pack(side='right', anchor='ne',expand=False, fill=None)
        self.entry_input()

    def fetch_data(self,id_channel):
        # Sélectionnez les colonnes 'heure_d_envoie' et 'message' de la table
        query=("SELECT user.surname , message.heure, message.message FROM message inner join user on message.id_user_emeteur=user.id where id_channel=%s")
        params=(id_channel,)
        rows = self.db.fetch(query,params)

        # Effacez le contenu actuel du Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ajoutez les nouvelles données au Treeview
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def entry_input(self):
        self.entry = Entry(self.root, width=90)
        self.entry.pack(pady=20, padx=100)
        self.entry.place(x=400, y=550)  # Positionner la barre d'entrée à x=100, y=50
        self.input = ""
    def get_input(self):
        # Utiliser la méthode get() pour récupérer le texte de l'Entry
        self.input = self.entry.get()
        print("Texte récupéré :", self.input)
        message.createMessage(self.input,self.id_user,self.number_channel)
        self.messaging()
    
    def up(self):
        if self.id_channel==self.channel.countAllChannel(self.id_user) - 1:
            self.id_channel=0
        else:
            self.id_channel+=1
        print(self.name_channel)
        self.number_channel=self.channel.numberChannelForUser(self.id_user)[self.id_channel][0]
        self.name_channel=self.channel.getNameChannel(self.number_channel)
        self.button.config(text=self.name_channel)
        self.messaging()

    def down(self):
        if self.id_channel==0:
            self.id_channel=self.channel.countAllChannel(self.id_user) - 1
        else:
            self.id_channel-=1
        print(self.id_channel)
        self.number_channel=self.channel.numberChannelForUser(self.id_user)[self.id_channel][0]
        self.name_channel=self.channel.getNameChannel(self.number_channel)
        self.button.config(text=self.name_channel)
        self.messaging()

    def main(self):
        # Définir la taille de la fenêtre
        self.root.geometry('1000x600')

        # Ajout d'un label à la fenêtre
        canvas = Canvas(self.root, width=1000, height=600)
        canvas.pack()

        # Dessiner un trait (ligne) sur le canvas
        canvas.create_line(333, 0, 333, 600, width=2, fill='black')

        # Créer un bouton pour créer la barre d'entrée
        self.button = Button(self.root, text=self.name_channel, command=self.messaging, width=46, height=5)
        self.button.pack(pady=40, padx=333)  # Ajout d'un espacement autour du bouton
        self.button.place(x=0, y=250)

        self.button_send = Button(self.root, text="Envoyer", command=self.get_input, width=10, height=5)
        self.button_send.pack(pady=40, padx=333)  # Ajout d'un espacement autour du bouton
        self.button_send.place(x=800, y=550)

        button_up = Button(self.root, text="^", command=self.up, width=46, height=5)
        button_up.pack(pady=0, padx=0)  # Ajout d'un espacement autour du bouton
        button_up.place(x=0, y=0)

        button_down = Button(self.root, text="v", command=self.down, width=46, height=5)
        button_down.pack(pady=0, padx=0)  # Ajout d'un espacement autour du bouton
        button_down.place(x=0, y=450)

        # Lancement de la boucle principale de la fenêtre
        self.root.mainloop()

# Créer une instance de la classe main_page et exécuter la méthode main
main = main_page()
message=Message()
if __name__ == "__main__":
    main.main()
