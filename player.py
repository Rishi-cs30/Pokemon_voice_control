# player.py

from pokemon import Pokemon


class Player:

    def __init__(self):
        self.pokemon_bag = []  # List to store the player's Pokémon
        self.badges = []  # List to store the badges the player has earned
        self.score = 0  # Player's score

    def add_pokemon(self, pokemon):
        """Add a Pokémon to the player's collection."""
        if len(self.pokemon_bag) < 6:  # A player can only have 6 Pokémon
            self.pokemon_bag.append(pokemon)
        else:
            print("You can only have 6 Pokémon at a time.")

    def remove_fainted_pokemon(self):
        """Remove fainted Pokémon from the player's collection."""
        self.pokemon_bag = [
            pokemon for pokemon in self.pokemon_bag
            if not pokemon.is_fainted()
        ]

    def choose_pokemon(self):
        """Let the player choose a Pokémon for battle."""
        self.remove_fainted_pokemon()  # Remove fainted Pokémon before choosing
        if not self.pokemon_bag:  # Check if the player has any Pokémon
            print("You have no Pokémon available!")
            return None
        print("Choose a Pokémon:")
        for i, p in enumerate(self.pokemon_bag, 1):
            print(f"{i}. {p}")
        while True:
            try:
                choice = int(input("Enter the number of your choice: ")) - 1
                if 0 <= choice < len(self.pokemon_bag):
                    return self.pokemon_bag[choice]
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

    def view_pokemon(self):
        """Display all the Pokémon the player currently has."""
        self.remove_fainted_pokemon()  # Remove fainted Pokémon before viewing
        if not self.pokemon_bag:  # Check if the player has no Pokémon
            print("You have no Pokémon.")
        else:
            print("Your Pokémon:")
            for p in self.pokemon_bag:  # Display each Pokémon
                print(p)
