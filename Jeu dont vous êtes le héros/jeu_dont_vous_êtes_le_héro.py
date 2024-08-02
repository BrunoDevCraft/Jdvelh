# main.py

from story import get_story_part, get_next_part, get_choice_text

def display_story(part_id):
    """Affiche la partie de l'histoire et les choix disponibles."""
    text, choices = get_story_part(part_id)
    print(text)
    
    if choices:
        print("\nChoisissez une option :")
        for key, value in choices.items():
            print(f"{key}: {value['text']}")
    else:
        print("\nFin de l'histoire. Voulez-vous recommencer ?")
        print("1: Oui (recommencer l'histoire)")
        print("2: Non (fermer le programme)")

def main():
    current_part_id = 1  # Commencer l'histoire à la partie 1

    while True:
        display_story(current_part_id)
        choices = get_story_part(current_part_id)[1]

        if choices:
            choice = input("\nEntrez le numéro de votre choix : ")
            next_part_id = get_next_part(current_part_id, choice)

            if next_part_id is not None:
                current_part_id = next_part_id
            else:
                print("Choix non valide. Veuillez essayer à nouveau.")
        else:
            restart_choice = input("\nEntrez '1' pour recommencer l'histoire ou '2' pour fermer le programme : ")

            if restart_choice == '1':
                current_part_id = 1  # Recommencer l'histoire
            elif restart_choice == '2':
                print("Merci d'avoir joué !")
                break
            else:
                print("Choix non valide. Veuillez entrer '1' pour recommencer ou '2' pour quitter.")

if __name__ == "__main__":
    main()
