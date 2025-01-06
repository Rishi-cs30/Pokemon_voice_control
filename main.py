#-------------------------------------------------------#
#Pokemon Adventure
#Version 02

#-------------------------------------------------------#
import random

# Define Pokemon class
class Pokemon:
    def __init__(self, name, p_type, health, moves):
        self.name = name
        self.type = p_type
        self.health = health
        self.moves = moves

    def take_damage(self, amount):
        self.health -= amount

    def heal(self, amount):
        self.health += amount

    def __str__(self):
        return f"{self.name} (Type: {self.type}, Health: {self.health}, Moves: {', '.join(self.moves)})"

# Define Player class
class Player:
    def __init__(self):
        self.pokemon_bag = []
        self.badges = []
        self.score = 0

    def catch_pokemon(self, pokemon):
        self.pokemon_bag.append(pokemon)
        self.score += 10  # Arbitrary score for catching a Pokemon

    def choose_pokemon(self):
        if self.pokemon_bag:
            return random.choice(self.pokemon_bag)
        return None

    def add_pokemon(self, pokemon):
        self.pokemon_bag.append(pokemon)

    def view_pokemon(self):
        if not self.pokemon_bag:
            print("You have no Pokémon.")
        else:
            for pokemon in self.pokemon_bag:
                print(pokemon)

# Define Game class
class Game:
    pokemon_dict = {
        'Pikachu': {'type': 'Electric', 'health': 35, 'moves': ['Thunder Shock', 'Quick Attack']},
        'Charmander': {'type': 'Fire', 'health': 39, 'moves': ['Ember', 'Scratch']},
        'Bulbasaur': {'type': 'Grass', 'health': 45, 'moves': ['Vine Whip', 'Tackle']},
        'Squirtle': {'type': 'Water', 'health': 44, 'moves': ['Water Gun', 'Tackle']},
        'Eevee': {'type': 'Normal', 'health': 55, 'moves': ['Tackle', 'Quick Attack']},
        'Jigglypuff': {'type': 'Fairy', 'health': 115, 'moves': ['Sing', 'Pound']},
        'Meowth': {'type': 'Normal', 'health': 40, 'moves': ['Scratch', 'Bite']},
        'Psyduck': {'type': 'Water', 'health': 50, 'moves': ['Water Gun', 'Confusion']},
        'Magikarp': {'type': 'Water', 'health': 20, 'moves': ['Splash', 'Tackle']},
        'Gengar': {'type': 'Ghost/Poison', 'health': 60, 'moves': ['Lick', 'Shadow Ball']}
    }

    def __init__(self):
        self.player = Player()

    def generate_pokemon(self):
        name = random.choice(list(self.pokemon_dict.keys()))
        stats = self.pokemon_dict[name]
        return Pokemon(name, stats['type'], stats['health'], stats['moves'])

    def attempt_catch(self, pokemon):
        success = random.choice([True, False])
        return success

    def wild_pokemon_encounter(self):
        wild_pokemon = self.generate_pokemon()
        print(f"You encountered a wild {wild_pokemon.name}!")

        action = input("Do you want to catch it or fight it? (catch/fight): ").lower()
        if action == 'catch':
            if self.attempt_catch(wild_pokemon):
                print(f"You caught {wild_pokemon.name}!")
                self.player.catch_pokemon(wild_pokemon)
            else:
                print(f"{wild_pokemon.name} escaped!")
        elif action == 'fight':
            player_pokemon = self.player.choose_pokemon()
            if player_pokemon:
                print(f"Go {player_pokemon.name}!")
                self.battle(player_pokemon, wild_pokemon)
            else:
                print("You have no Pokémon to battle with!")
        else:
            print("Invalid action. Please choose 'catch' or 'fight'.")

    def battle(self, player_pokemon, wild_pokemon):
        while player_pokemon.health > 0 and wild_pokemon.health > 0:
            print(f"{player_pokemon.name} HP: {player_pokemon.health} | {wild_pokemon.name} HP: {wild_pokemon.health}")
            move = input(f"Choose {player_pokemon.name}'s move ({'/'.join(player_pokemon.moves)}): ").strip()
            if move in player_pokemon.moves:
                damage = 10  # Fixed damage for simplicity
                wild_pokemon.take_damage(damage)
                print(f"{player_pokemon.name} used {move}! {wild_pokemon.name} took {damage} damage.")
            else:
                print(f"{player_pokemon.name} doesn't know that move!")

            if wild_pokemon.health > 0:
                opponent_move = random.choice(wild_pokemon.moves)
                damage = 10  # Fixed damage for simplicity
                player_pokemon.take_damage(damage)
                print(f"{wild_pokemon.name} used {opponent_move}! {player_pokemon.name} took {damage} damage.")

        if player_pokemon.health > 0:
            print(f"{player_pokemon.name} won the battle!")
        else:
            print(f"{wild_pokemon.name} won the battle!")

    def choose_starter_pokemon(self):
        starter_options = ['Pikachu', 'Charmander', 'Bulbasaur']
        print("Choose your starter Pokémon:")
        for i, name in enumerate(starter_options, start=1):
            print(f"{i}. {name}")

        choice = int(input("Enter the number of your choice: ")) - 1
        chosen_name = starter_options[choice]
        stats = self.pokemon_dict[chosen_name]
        starter_pokemon = Pokemon(chosen_name, stats['type'], stats['health'], stats['moves'])
        self.player.add_pokemon(starter_pokemon)
        print(f"You chose {starter_pokemon.name} as your starter Pokémon!")

    def display_menu(self):
        print("Main Menu:")
        print("1. Wild Pokémon Encounter")
        print("2. View Pokémon")
        print("3. Gym Challenge")
        print("4. View High Scores")
        print("5. Exit Game")

    def start_game(self):
        print("Welcome to the Pokémon Adventure Game!")
        self.choose_starter_pokemon()
        while True:
            self.display_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                self.wild_pokemon_encounter()
            elif choice == '2':
                self.player.view_pokemon()
            elif choice == '3':
                # Gym challenge not implemented in version 2
                print("Gym challenge feature not available in this version.")
            elif choice == '4':
                print(f"High Scores: {self.player.score}")
            elif choice == '5':
                print("Exiting game...")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    game = Game()
    game.start_game()
import random

# Define Pokemon class
class Pokemon:
    def __init__(self, name, p_type, health, moves):
        self.name = name
        self.type = p_type
        self.health = health
        self.moves = moves

    def take_damage(self, amount):
        self.health -= amount

    def heal(self, amount):
        self.health += amount

    def __str__(self):
        return f"{self.name} (Type: {self.type}, Health: {self.health}, Moves: {', '.join(self.moves)})"

# Define Player class
class Player:
    def __init__(self):
        self.pokemon_bag = []
        self.badges = []
        self.score = 0

    def catch_pokemon(self, pokemon):
        self.pokemon_bag.append(pokemon)
        self.score += 10  # Arbitrary score for catching a Pokemon

    def choose_pokemon(self):
        if self.pokemon_bag:
            return random.choice(self.pokemon_bag)
        return None

    def add_pokemon(self, pokemon):
        self.pokemon_bag.append(pokemon)

    def view_pokemon(self):
        if not self.pokemon_bag:
            print("You have no Pokémon.")
        else:
            for pokemon in self.pokemon_bag:
                print(pokemon)

# Define Game class
class Game:
    pokemon_dict = {
        'Pikachu': {'type': 'Electric', 'health': 35, 'moves': ['Thunder Shock', 'Quick Attack']},
        'Charmander': {'type': 'Fire', 'health': 39, 'moves': ['Ember', 'Scratch']},
        'Bulbasaur': {'type': 'Grass', 'health': 45, 'moves': ['Vine Whip', 'Tackle']},
        'Squirtle': {'type': 'Water', 'health': 44, 'moves': ['Water Gun', 'Tackle']},
        'Eevee': {'type': 'Normal', 'health': 55, 'moves': ['Tackle', 'Quick Attack']},
        'Jigglypuff': {'type': 'Fairy', 'health': 115, 'moves': ['Sing', 'Pound']},
        'Meowth': {'type': 'Normal', 'health': 40, 'moves': ['Scratch', 'Bite']},
        'Psyduck': {'type': 'Water', 'health': 50, 'moves': ['Water Gun', 'Confusion']},
        'Magikarp': {'type': 'Water', 'health': 20, 'moves': ['Splash', 'Tackle']},
        'Gengar': {'type': 'Ghost/Poison', 'health': 60, 'moves': ['Lick', 'Shadow Ball']}
    }

    def __init__(self):
        self.player = Player()

    def generate_pokemon(self):
        name = random.choice(list(self.pokemon_dict.keys()))
        stats = self.pokemon_dict[name]
        return Pokemon(name, stats['type'], stats['health'], stats['moves'])

    def attempt_catch(self, pokemon):
        success = random.choice([True, False])
        return success

    def wild_pokemon_encounter(self):
        wild_pokemon = self.generate_pokemon()
        print(f"You encountered a wild {wild_pokemon.name}!")

        action = input("Do you want to catch it or fight it? (catch/fight): ").lower()
        if action == 'catch':
            if self.attempt_catch(wild_pokemon):
                print(f"You caught {wild_pokemon.name}!")
                self.player.catch_pokemon(wild_pokemon)
            else:
                print(f"{wild_pokemon.name} escaped!")
        elif action == 'fight':
            player_pokemon = self.player.choose_pokemon()
            if player_pokemon:
                print(f"Go {player_pokemon.name}!")
                self.battle(player_pokemon, wild_pokemon)
            else:
                print("You have no Pokémon to battle with!")
        else:
            print("Invalid action. Please choose 'catch' or 'fight'.")

    def battle(self, player_pokemon, wild_pokemon):
        while player_pokemon.health > 0 and wild_pokemon.health > 0:
            print(f"{player_pokemon.name} HP: {player_pokemon.health} | {wild_pokemon.name} HP: {wild_pokemon.health}")
            move = input(f"Choose {player_pokemon.name}'s move ({'/'.join(player_pokemon.moves)}): ").strip()
            if move in player_pokemon.moves:
                damage = 10  # Fixed damage for simplicity
                wild_pokemon.take_damage(damage)
                print(f"{player_pokemon.name} used {move}! {wild_pokemon.name} took {damage} damage.")
            else:
                print(f"{player_pokemon.name} doesn't know that move!")

            if wild_pokemon.health > 0:
                opponent_move = random.choice(wild_pokemon.moves)
                damage = 10  # Fixed damage for simplicity
                player_pokemon.take_damage(damage)
                print(f"{wild_pokemon.name} used {opponent_move}! {player_pokemon.name} took {damage} damage.")

        if player_pokemon.health > 0:
            print(f"{player_pokemon.name} won the battle!")
        else:
            print(f"{wild_pokemon.name} won the battle!")

    def choose_starter_pokemon(self):
        starter_options = ['Pikachu', 'Charmander', 'Bulbasaur']
        print("Choose your starter Pokémon:")
        for i, name in enumerate(starter_options, start=1):
            print(f"{i}. {name}")

        choice = int(input("Enter the number of your choice: ")) - 1
        chosen_name = starter_options[choice]
        stats = self.pokemon_dict[chosen_name]
        starter_pokemon = Pokemon(chosen_name, stats['type'], stats['health'], stats['moves'])
        self.player.add_pokemon(starter_pokemon)
        print(f"You chose {starter_pokemon.name} as your starter Pokémon!")

    def display_menu(self):
        print("Main Menu:")
        print("1. Wild Pokémon Encounter")
        print("2. View Pokémon")
        print("3. Gym Challenge")
        print("4. View High Scores")
        print("5. Exit Game")

    def start_game(self):
        print("Welcome to the Pokémon Adventure Game!")
        self.choose_starter_pokemon()
        while True:
            self.display_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                self.wild_pokemon_encounter()
            elif choice == '2':
                self.player.view_pokemon()
            elif choice == '3':
                # Gym challenge not implemented in version 2
                print("Gym challenge feature not available in this version.")
            elif choice == '4':
                print(f"High Scores: {self.player.score}")
            elif choice == '5':
                print("Exiting game...")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    game = Game()
    game.start_game()
