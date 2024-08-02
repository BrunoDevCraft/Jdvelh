import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import os
from story import get_story_part, get_next_part

class AdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Vous êtes un Héros")
        self.current_part_id = 1

        # Configurer la taille minimale de la fenêtre
        self.root.geometry("600x600")  # Augmenter la hauteur pour accueillir les images

        # Configurer la grille
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.start_screen()

    def start_screen(self):
        """Affiche la page de présentation."""
        self.clear_screen()

        title = tk.Label(self.root, text="Le jeu\n" "dont\n" "Vous êtes le Héros", font=("Helvetica", 36))
        title.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        start_button = tk.Button(self.root, text="Démarrer l'histoire", font=("Helvetica", 18), command=self.start_story)
        start_button.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        quit_button = tk.Button(self.root, text="Fermer le jeu", font=("Helvetica", 18), command=self.root.quit)
        quit_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

    def start_story(self):
        """Commence l'histoire en affichant la première partie."""
        self.clear_screen()
        self.display_story(self.current_part_id)

    def display_story(self, part_id):
        """Affiche la partie de l'histoire et les choix disponibles."""
        text, choices, image_path = get_story_part(part_id)

        if text is None or choices is None:
            messagebox.showerror("Erreur", "Partie d'histoire non valide.")
            return

        # Affichage de l'image associée à la partie de l'histoire
        if image_path and os.path.exists(image_path):
            try:
                image = PhotoImage(file=image_path)
                if hasattr(self, 'image_label') and self.image_label is not None:
                    self.image_label.config(image=image)
                    self.image_label.image = image  # Prévenir le garbage collection
                else:
                    self.image_label = tk.Label(self.root, image=image)
                    self.image_label.grid(row=0, column=0, padx=20, pady=(10, 5), sticky="nwe")
                    self.image_label.image = image  # Prévenir le garbage collection
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de charger l'image : {e}")
        else:
            if hasattr(self, 'image_label') and self.image_label is not None:
                self.image_label.destroy()
                self.image_label = None

        # Mise à jour du texte de l'histoire
        if hasattr(self, 'text_label') and self.text_label is not None:
            self.text_label.config(text=text)
        else:
            self.text_label = tk.Label(self.root, text=text, wraplength=500, font=("Helvetica", 14), justify="left")
            self.text_label.grid(row=1, column=0, padx=20, pady=(5, 20), sticky="nwe")

        # Effacement des boutons de choix précédents
        if hasattr(self, 'choice_buttons'):
            for button in self.choice_buttons:
                button.destroy()
        self.choice_buttons = []

        # Initialisation de row_index
        row_index = 2

        # Création des nouveaux boutons de choix
        if choices:
            for key, value in choices.items():
                button = tk.Button(self.root, text=value['text'], font=("Helvetica", 14), command=lambda k=key: self.make_choice(k))
                button.grid(row=row_index, column=0, padx=20, pady=5, sticky="ew")
                row_index += 1
                self.choice_buttons.append(button)
        else:
            restart_button = tk.Button(self.root, text="Recommencer l'histoire", font=("Helvetica", 18), command=self.restart_story)
            restart_button.grid(row=row_index, column=0, padx=20, pady=10, sticky="ew")

            quit_button = tk.Button(self.root, text="Fermer le jeu", font=("Helvetica", 18), command=self.root.quit)
            quit_button.grid(row=row_index+1, column=0, padx=20, pady=10, sticky="ew")

    def make_choice(self, choice_key):
        """Gère le choix de l'utilisateur et passe à la partie suivante."""
        next_part_id = get_next_part(self.current_part_id, choice_key)
        if next_part_id is not None:
            self.current_part_id = next_part_id
            self.display_story(next_part_id)
        else:
            messagebox.showerror("Erreur", "Choix non valide. Veuillez essayer à nouveau.")

    def restart_story(self):
        """Redémarre l'histoire depuis le début."""
        self.current_part_id = 1
        self.start_story()

    def clear_screen(self):
        """Efface tous les widgets de la fenêtre sauf la barre de titre."""
        for widget in self.root.winfo_children():
            widget.destroy()
        self.text_label = None
        self.choice_buttons = []
        self.image_label = None

if __name__ == "__main__":
    root = tk.Tk()
    game = AdventureGame(root)
    root.mainloop()
