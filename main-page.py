from tkinter import *
from channel import Channel
from db import Db

class main_page:
    
    def __init__(self):
        # Création de la fenêtre principale
        self.db=Db('ilyes-chabab.students-laplateforme.io','ilyes-chabab','Nitrate13140','ilyes-chabab_myDiscord')
        self.channel=Channel()
        self.root = Tk()
        self.root.title('main-page') 
        self.id_user=1
        self.id_channel=0
        self.number_channel=self.channel.numberChannelForUser(self.id_user)[self.id_channel][0]
        self.name_channel=self.channel.getNameChannel(self.number_channel)

    def create_input_bar(self):
        print(self.name_channel)
        entry = Entry(self.root, width=90)
        entry.pack(pady=20, padx=100)
        entry.place(x=400, y=550)  # Positionner la barre d'entrée à x=100, y=50
    
    def up(self):
        if self.id_channel==self.channel.countAllChannel(self.id_user) - 1:
            self.id_channel=0
        else:
            self.id_channel+=1
        print(self.name_channel)
        self.number_channel=self.channel.numberChannelForUser(self.id_user)[self.id_channel][0]
        self.name_channel=self.channel.getNameChannel(self.number_channel)
        self.button.config(text=self.name_channel)

    def down(self):
        if self.id_channel==0:
            self.id_channel=self.channel.countAllChannel(self.id_user) - 1
        else:
            self.id_channel-=1
        print(self.id_channel)
        self.number_channel=self.channel.numberChannelForUser(self.id_user)[self.id_channel][0]
        self.name_channel=self.channel.getNameChannel(self.number_channel)
        self.button.config(text=self.name_channel)

    def main(self):
       
        # Définir la taille de la fenêtre
        self.root.geometry('1000x600')

        # Ajout d'un label à la fenêtre
        canvas = Canvas(self.root, width=1000, height=600)
        canvas.pack()

        # Dessiner un trait (ligne) sur le canvas
        canvas.create_line(333, 0, 333, 600, width=2, fill='black')

        # Créer un bouton pour créer la barre d'entrée
        self.button = Button(self.root, text=self.name_channel, command=self.create_input_bar, width=46, height=5)
        self.button.pack(pady=40, padx=333)  # Ajout d'un espacement autour du bouton
        self.button.place(x=0, y=250)

        button_up = Button(self.root, text="^", command=self.up, width=46, height=5)
        button_up.pack(pady=40, padx=333)  # Ajout d'un espacement autour du bouton
        button_up.place(x=0, y=0)

        button_down = Button(self.root, text="v", command=self.down, width=46, height=5)
        button_down.pack(pady=40, padx=333)  # Ajout d'un espacement autour du bouton
        button_down.place(x=0, y=450)
        
        # Créer une barre d'entrée initiale, mais la masquer
        

        # Lancement de la boucle principale de la fenêtre
        self.root.mainloop()

main = main_page()
if __name__ == "__main__":
    main.main()
