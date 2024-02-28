from tkinter import *

class main_page:
    
    def __init__(self):
        # Création de la fenêtre principale
        self.root = Tk()
        self.root.title('main-page')

    def create_input_bar(self):
        print('jskg')
        entry = Entry(self.root, width=90)
        entry.pack(pady=20, padx=100)
        entry.place(x=400, y=550)  # Positionner la barre d'entrée à x=100, y=50

    def main(self):
       
        # Définir la taille de la fenêtre
        self.root.geometry('1000x600')

        # Ajout d'un label à la fenêtre
        canvas = Canvas(self.root, width=1000, height=600)
        canvas.pack()

        # Dessiner un trait (ligne) sur le canvas
        canvas.create_line(333, 0, 333, 600, width=2, fill='black')

        # Créer un bouton pour créer la barre d'entrée
        button = Button(self.root, text='Cliquez-moi', command=self.create_input_bar, width=46, height=5)
        button.pack(pady=40, padx=333)  # Ajout d'un espacement autour du bouton
        button.place(x=0, y=0)
        
        # Créer une barre d'entrée initiale, mais la masquer
        

        # Lancement de la boucle principale de la fenêtre
        self.root.mainloop()

main = main_page()
if __name__ == "__main__":
    main.main()
