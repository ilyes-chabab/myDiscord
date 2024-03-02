from tkinter import Tk, Entry, Button

class MaClasse:
    def __init__(self):
        self.root = Tk()
        self.entry = Entry(self.root, width=90)
        self.entry.pack(pady=20, padx=100)
        self.entry.place(x=400, y=550)

        # Créer un bouton qui, lorsqu'il est cliqué, récupère le texte de l'Entry
        button_recuperer = Button(self.root, text="Récupérer le texte", command=self.recuperer_texte)
        button_recuperer.pack()

        # Variable pour stocker le texte de l'Entry
        self.texte_recupere = ""

        self.root.mainloop()

    def recuperer_texte(self):
        # Utiliser la méthode get() pour récupérer le texte de l'Entry
        self.texte_recupere = self.entry.get()
        print("Texte récupéré :", self.texte_recupere)

# Créer une instance de la classe
app = MaClasse()
