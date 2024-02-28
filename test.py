from tkinter import Tk, Button

def on_button_click():
    print("Bouton cliqué !")

def main():
    # Création de la fenêtre principale
    root = Tk()
    root.title('Exemple de bouton Tkinter')
    
    # Création d'un bouton
    button = Button(root, text='Cliquez-moi', command=on_button_click)
    button.pack(pady=20, padx=50)  # Ajout d'un espacement autour du bouton
    
    # Lancement de la boucle principale de la fenêtre
    root.mainloop()

if __name__ == "__main__":
    main()
