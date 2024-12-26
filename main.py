import random

# Class to represent a Pokémon
class Pokemon:
    def __init__(self, name, pokemon_type, health):
        self.name = name
        self.type = pokemon_type
        self.health = health

    def __str__(self):
        return f"{self.name} (Type: {self.type}, Health: {self.health})"

# Class to represent the Trainer
class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon_bag = []

    def catch_pokemon(self, pokemon):
        self.pokemon_bag.append(pokemon)
        print(f"{pokemon.name} was added to your bag!")

    def view_pokemon(self):
        if not self.pokemon_bag:
            print("Your bag is empty!")
        else:
            print("Your Pokémon:")
            for idx, pokemon in enumerate(self.pokemon_bag, 1):
                print(f"{idx}. {pokemon}")

# Class to represent the Game
class Game:
    def __init__(self):
        self.trainer = Trainer(input("Enter your name, Trainer: "))
        # Wild Pokémon dictionary with name as key and type/health as value
        self.wild_pokemon_dict = {
            "Pikachu": {"type": "Electric", "health": 50},
            "Charmander": {"type": "Fire", "health": 60},
            "Squirtle": {"type": "Water", "health": 55},
            "Bulbasaur": {"type": "Grass", "health": 58},
        }

    def start_game(self):
        print(f"Welcome, {self.trainer.name}, to the Pokémon Adventure!")
        while True:
            print("\nMain Menu:")
            print("1. Wild Pokémon Encounter")
            print("2. View Caught Pokémon")
            print("3. Exit Game")
            choice = input("Choose an option: ").lower()

            if choice in ["1", "wild pokemon encounter"]:
                self.wild_pokemon_encounter()
            elif choice in ["2", "view caught pokemon"]:
                self.trainer.view_pokemon()
            elif choice in ["3", "exit game"]:
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

    def wild_pokemon_encounter(self):
        # Randomly select a Pokémon from the dictionary
        pokemon_name, pokemon_stats = random.choice(list(self.wild_pokemon_dict.items()))
        wild_pokemon = Pokemon(pokemon_name, pokemon_stats["type"], pokemon_stats["health"])
        print(f"\nA wild {wild_pokemon.name} appeared!")
        while True:
            action = input("Do you want to catch it? (yes/no): ").lower()
            if action == "yes":
                if random.random() > 0.5:
                    print(f"Success! You caught {wild_pokemon.name}.")
                    self.trainer.catch_pokemon(wild_pokemon)
                else:
                    print(f"{wild_pokemon.name} escaped!")
                break
            elif action == "no":
                print(f"You let {wild_pokemon.name} go.")
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

# Initialize and start the game
if __name__ == "__main__":
    game = Game()
    game.start_game()
