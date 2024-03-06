from tkinter import *
from tkinter import ttk
import tkinter as tk
from Channel import Channel
from Db import Db
from Message import Message
from Right import Right

class main_page:
    
    def __init__(self):
        # Création de la fenêtre principale
        self.db=Db('ilyes-chabab.students-laplateforme.io','ilyes-chabab','Nitrate13140','ilyes-chabab_myDiscord')
        self.channel=Channel()
        self.root = tk.Tk()
        self.root.title('myDiscord') 
        self.id_user=2
        self.id_channel=0
        self.number_channel=self.channel.numberChannelForUser(self.id_user)[self.id_channel][0]
        self.name_channel=self.channel.getNameChannel(self.number_channel)
        self.tree = ttk.Treeview(self.root, columns= ('id_user_emeteur','heure', 'message'))
        self.messaging()

    def messaging(self):
        print("jqshd")
        self.tree.column('id_user_emeteur', anchor='center', width=50)  # Ajustez la largeur 
        self.tree.column('heure', anchor='center', width=150)
        self.tree.column('message', anchor='w', width=400)  # 'w' signifie west : alignement à gauche (left)
        # Remplissez le Treeview avec les données
        self.fetch_data(self.number_channel)
        # Ajoutez le Treeview à la fenêtre principale
        self.tree.pack(side='right', anchor='ne',expand=False, fill=None )
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
        self.max_caracteres = 65  # Définissez le nombre maximum de caractères autorisés

        self.entry_var = StringVar()
        self.entry = Entry(self.root, width=90, textvariable=self.entry_var)
        self.entry.pack(pady=20, padx=50)
        self.entry.place(x=500, y=550)  # Positionner la barre d'entrée 

        # Configurez la validation pour limiter le nombre de caractères
        self.entry_var.trace_add("write", self.valid_entry)

    def valid_entry(self, *args):
        new_valeur = self.entry_var.get()
        if len(new_valeur) > self.max_caracteres:
            self.entry_var.set(new_valeur[:self.max_caracteres])

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
    
    def create_channel_main(self):
        self.input_name_channel = self.entry_channel.get()
        print("Texte récupéré :", self.input_name_channel)
        name_channel=self.input_name_channel
        channel.createChannel(name_channel)
        id_of_channel=channel.getNameChannelWithName(name_channel)[::-1][0][0]
        right.createCreator(id_of_channel,self.id_user)

    
    def clear_text_entry_channel(self, event):
        # Effacer le texte lorsqu'on clique sur le champ de saisie
        self.entry_channel.delete(0, tk.END)

        
    def clear_text_entry_add_user(self, event):
        # Effacer le texte lorsqu'on clique sur le champ de saisie
        self.entry_add_user.delete(0, tk.END)

    def clear_text_entry_kick_user(self,event):
        # Effacer le texte lorsqu'on clique sur le champ de saisie
        self.entry_kick_user.delete(0, tk.END)
    
    def clear_text_entry_put_admin_user(self,event):
        # Effacer le texte lorsqu'on clique sur le champ de saisie
        self.entry_put_admin_user.delete(0, tk.END)

    def clear_text_entry_remove_admin_user(self,event):
        # Effacer le texte lorsqu'on clique sur le champ de saisie
        self.entry_remove_admin_user.delete(0, tk.END)

    def add_user_main(self):
        self.input_name_user_add=self.entry_add_user.get()
        print(self.input_name_user_add)
        id_of_user=right.getIdUser(self.input_name_user_add)[0][0]
        right.addUser(self.number_channel,id_of_user)

    def kick_user_main(self):
        self.input_name_user_kick=self.entry_kick_user.get()
        print(self.input_name_user_kick)
        id_of_user=right.getIdUser(self.input_name_user_kick)[0][0]
        print(self.number_channel)
        print(id_of_user)
        if right.getRightNumber(self.number_channel,self.id_user)[0][0]==1: #si l'utilisateur qui fait la requete est admin
            right.deleteUser(self.number_channel,id_of_user)
            print(f'{self.input_name_user_kick} a été expulsé')
        else:
            print("l'utilisateur n'a pas les droits necessaires")
        
    
    def put_admin_user_main(self):
        self.input_admin_user=self.entry_put_admin_user.get()
        print(self.input_admin_user)
        id_of_user=right.getIdUser(self.input_admin_user)[0][0]
        print(self.number_channel)
        print(id_of_user)
        print(right.getRightNumber(self.number_channel,self.id_user)[0][0])
        if right.getRightNumber(self.number_channel,self.id_user)[0][0]==1: #si l'utilisateur qui fait la requete est admin
            right.updateRight(1,self.number_channel,id_of_user)
            print(f'{self.input_admin_user} est devenue admin')
        else:
            print("l'utilisateur n'a pas les droits necessaires")
        print(right.readRight())
    
    def remove_admin_user_main(self):
        self.input_remove_admin_user=self.entry_remove_admin_user.get()
        print(self.input_remove_admin_user)
        id_of_user=right.getIdUser(self.input_remove_admin_user)[0][0]
        print(self.number_channel)
        print(id_of_user)
        print(right.getRightNumber(self.number_channel,self.id_user)[0][0])
        if right.getRightNumber(self.number_channel,self.id_user)[0][0]==1: #si l'utilisateur qui fait la requete est admin
            right.updateRight(2,self.number_channel,id_of_user)
            print(f"{self.input_remove_admin_user} est devenue membre")
        else:
            print("l'utilisateur n'a pas les droits necessaires")
        print(right.readRight())
    
    def deconnection(self):
        print("deconnection")

    def remove_channel_main(self):
        if right.getRightNumber(self.number_channel,self.id_user)[0][0]==1: #si l'utilisateur qui fait la requete est admin
            print(self.number_channel)
            numberOfChannel=self.number_channel
            channel.deleteChannel(numberOfChannel)
            self.up()
            right.deleteAllUser(numberOfChannel)
            print(f"le channel avec n° {numberOfChannel} a été supprimé")    
        else:
            print("l'utilisateur n'a pas les droits necessaires")

    #partie interface :
            
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
        self.button.place(x=0, y=400)
    
        self.button_create_channel = Button(self.root, text="Creer", command=self.create_channel_main, width=10, height=1)
        self.button_create_channel.pack(pady=40, padx=333)  # Ajout d'un espacement autour du bouton
        self.button_create_channel.place(x=240, y=120)

        self.button_remove_channel = Button(self.root, text="supprimer", command=self.remove_channel_main, width=10, height=1)
        self.button_remove_channel.pack(pady=40, padx=333)  # Ajout d'un espacement autour du bouton
        self.button_remove_channel.place(x=340, y=120)

        self.entry_channel = Entry(self.root, width=40)
        self.entry_channel.pack(pady=20, padx=100)
        self.entry_channel.place(x=10, y=120)
        self.entry_channel.insert(0, "Nom du channel")
        self.entry_channel.bind("<Button-1>", self.clear_text_entry_channel)
        self.input_name_channel=''

        self.button_add_user = Button(self.root, text="ajouter ", command=self.add_user_main, width=10, height=1)
        self.button_add_user.pack(pady=40, padx=333)  # Ajout d'un espacement autour du bouton
        self.button_add_user.place(x=240, y=180)

        self.entry_add_user = Entry(self.root, width=40)
        self.entry_add_user.pack(pady=20, padx=100)
        self.entry_add_user.place(x=10, y=180)
        self.entry_add_user.insert(0, "nom de l'utilisateur")
        self.entry_add_user.bind("<Button-1>", self.clear_text_entry_add_user)
        self.input_name_user_add=''

        self.button_kick_user = Button(self.root, text="expulser ", command=self.kick_user_main, width=10, height=1)
        self.button_kick_user.pack(pady=40, padx=333)  # Ajout d'un espacement autour du bouton
        self.button_kick_user.place(x=240, y=240)

        self.entry_kick_user = Entry(self.root, width=40)
        self.entry_kick_user.pack(pady=20, padx=100)
        self.entry_kick_user.place(x=10, y=240)
        self.entry_kick_user.insert(0, "nom de l'utilisateur")
        self.entry_kick_user.bind("<Button-1>", self.clear_text_entry_kick_user)
        self.input_name_user_kick=''

        self.button_put_admin_user = Button(self.root, text="mettre ", command=self.put_admin_user_main, width=10, height=1)
        self.button_put_admin_user.pack(pady=40, padx=333)  # Ajout d'un espacement autour du bouton
        self.button_put_admin_user.place(x=240, y=300)

        self.entry_put_admin_user = Entry(self.root, width=40)
        self.entry_put_admin_user.pack(pady=20, padx=100)
        self.entry_put_admin_user.place(x=10, y=300)
        self.entry_put_admin_user.insert(0, "nom de l'utilisateur")
        self.entry_put_admin_user.bind("<Button-1>", self.clear_text_entry_put_admin_user)
        self.input_admin_user=''

        self.button_remove_admin_user = Button(self.root, text="enlever ", command=self.remove_admin_user_main, width=10, height=1)
        self.button_remove_admin_user.pack(pady=40, padx=333)  # Ajout d'un espacement autour du bouton
        self.button_remove_admin_user.place(x=240, y=360)

        self.entry_remove_admin_user = Entry(self.root, width=40)
        self.entry_remove_admin_user.pack(pady=20, padx=100)
        self.entry_remove_admin_user.place(x=10, y=360)
        self.entry_remove_admin_user.insert(0, "nom de l'utilisateur")
        self.entry_remove_admin_user.bind("<Button-1>", self.clear_text_entry_remove_admin_user)
        self.input_remove_user=''

        # Création d'un label
        label_create_channel = tk.Label(self.root, text="Creer un channel :", font=("Arial", 12))
        # Placement du label à un endroit précis (en pixels)
        label_create_channel.place(x=0, y=90)

        label_create_channel = tk.Label(self.root, text="supprimer un channel :", font=("Arial", 10))
        label_create_channel.place(x=340, y=90)

        label_add_user = tk.Label(self.root, text="ajouter un utilisateur :", font=("Arial", 12))
        label_add_user.place(x=0, y=150)

        label_kick_user = tk.Label(self.root, text="expulsez un utilisateur :", font=("Arial", 12))
        label_kick_user.place(x=0, y=210)

        label_kick_user = tk.Label(self.root, text="ajouter un admin :", font=("Arial", 12))
        label_kick_user.place(x=0, y=270)

        label_remove_admin_user = tk.Label(self.root, text="enlever un admin :", font=("Arial", 12))
        label_remove_admin_user.place(x=0, y=330)

        label_remove_account_of = tk.Label(self.root, text="compte de :", font=("Arial", 12))
        label_remove_account_of.place(x=350, y=450)

        self.name= right.getNameUser(self.id_user)
        label_remove_account_of_name = tk.Label(self.root, text=self.name, font=("Arial", 11))
        label_remove_account_of_name.place(x=350, y=480)

        self.button_send = Button(self.root, text="Envoyer", command=self.get_input, width=10, height=1)
        self.button_send.pack(pady=40, padx=333)  # Ajout d'un espacement autour du bouton
        self.button_send.place(x=1000, y=550)

        self.button_deconnection = Button(self.root, text="Déconnection", command=self.deconnection, width=10, height=1)
        self.button_deconnection.pack(pady=40, padx=333)  # Ajout d'un espacement autour du bouton
        self.button_deconnection.place(x=350, y=550)

        button_up = Button(self.root, text="^", command=self.up, width=46, height=5)
        button_up.pack(pady=0, padx=0)  # Ajout d'un espacement autour du bouton
        button_up.place(x=0, y=0)

        button_down = Button(self.root, text="v", command=self.down, width=46, height=5)
        button_down.pack(pady=0, padx=0)  # Ajout d'un espacement autour du bouton
        button_down.place(x=0, y=510)

        # Lancement de la boucle principale de la fenêtre
        self.root.mainloop()

# Créer une instance de la classe main_page et exécuter la méthode main
main = main_page()
message=Message()
channel=Channel()
right=Right()

main.main()
