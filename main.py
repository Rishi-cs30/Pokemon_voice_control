import random
import pyttsx3

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Setting properties 
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (1.0)

# Pokemon dictionary with various Pokemon
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

# Type effectiveness chart
type_chart = {
    "Water": {"Fire": 2, "Rock": 2, "Grass": 0.5},
    "Fire": {"Grass": 2, "Water": 0.5, "Rock": 0.5},
    "Grass": {"Water": 2, "Rock": 2, "Fire": 0.5},
    "Rock": {"Fire": 2, "Water": 0.5, "Grass": 0.5}
}

def speak(text):
    engine.say(text)
    engine.runAndWait()

class Pokemon:
    def __init__(self, name, type_, health, moves):
        self.name = name
        self.type = type_
        self.health = health
        self.moves = moves

    def __str__(self):
        return f"{self.name} ({self.type}) - HP: {self.health}"

    def is_fainted(self):
        return self.health <= 0

class Player:
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.badges = []
        self.score = 0

    def choose_pokemon(self):
        if not self.pokemon:
            speak("You have no Pokémon left to fight!")
            return None
        speak("Your Pokémon:")
        for i, p in enumerate(self.pokemon):
            if not p.is_fainted():
                speak(f"{i + 1}. {p}")
        choice = int(input("Choose your Pokémon by number: ")) - 1
        if 0 <= choice < len(self.pokemon) and not self.pokemon[choice].is_fainted():
            return self.pokemon[choice]
        speak("Invalid choice.")
        return None

    def view_pokemon(self):
        if not self.pokemon:
            speak("You don't have any Pokémon yet!")
            return
        speak("Your Pokémon:")
        for p in self.pokemon:
            speak(f"- {p}")

    def remove_fainted_pokemon(self):
        # Remove Pokemon with 0 health from the team
        self.pokemon = [p for p in self.pokemon if not p.is_fainted()]

class Game:
    def __init__(self):
        self.player = None

    def calculate_damage(self, attacker, defender, move):
        base_damage = random.randint(10, 20)
        type_effectiveness = type_chart.get(attacker.type, {}).get(defender.type, 1)
        return int(base_damage * type_effectiveness)

    def battle(self, player_pokemon, wild_pokemon):
        speak(f"A wild {wild_pokemon} appeared!")

        while not player_pokemon.is_fainted() and not wild_pokemon.is_fainted():
            speak(f"Your {player_pokemon} vs Wild {wild_pokemon}")

            # Player's turn
            speak("Your moves:")
            for i, move in enumerate(player_pokemon.moves):
                speak(f"{i + 1}. {move}")
            move_choice = int(input("Choose a move: ")) - 1

            if 0 <= move_choice < len(player_pokemon.moves):
                damage = self.calculate_damage(player_pokemon, wild_pokemon, player_pokemon.moves[move_choice])
                wild_pokemon.health -= damage
                speak(f"{player_pokemon.name} used {player_pokemon.moves[move_choice]} and dealt {damage} damage!")
            else:
                speak("Invalid move choice.")

            if wild_pokemon.is_fainted():
                speak(f"The wild {wild_pokemon.name} fainted!")
                self.player.score += 10
                break

            # Wild Pokemon's turn
            wild_move = random.choice(wild_pokemon.moves)
            damage = self.calculate_damage(wild_pokemon, player_pokemon, wild_move)
            player_pokemon.health -= damage
            speak(f"The wild {wild_pokemon.name} used {wild_move} and dealt {damage} damage!")

            if player_pokemon.is_fainted():
                speak(f"Your {player_pokemon.name} fainted!")
                break

        # Remove any fainted Pokemon from the player's team
        self.player.remove_fainted_pokemon()

    def explore_wild(self):
        speak("Exploring the wild...")

        # Randomly select a wild Pokemon from pokemon_dict
        wild_pokemon_name = random.choice(list(pokemon_dict.keys()))
        wild_pokemon_data = pokemon_dict[wild_pokemon_name]
        wild_pokemon = Pokemon(wild_pokemon_name, wild_pokemon_data['type'], wild_pokemon_data['health'], wild_pokemon_data['moves'])

        speak(f"A wild {wild_pokemon.name} appeared!")

        choice = input("Do you want to (1) Catch or (2) Fight the Pokémon? ")

        if choice == "1":
            if random.random() < 0.8:  # 80% chance to catch
                speak(f"Congratulations! You caught the wild {wild_pokemon.name}!")
                self.player.pokemon.append(wild_pokemon)
            else:
                speak(f"Oh no! The wild {wild_pokemon.name} escaped!")
        elif choice == "2":
            player_pokemon = self.player.choose_pokemon()
            if player_pokemon:
                self.battle(player_pokemon, wild_pokemon)
        else:
            speak("Invalid choice. The wild Pokémon ran away.")

    def gym_challenge(self):
        speak("Welcome to the Pewter Gym!")
        gym_leader = "Brock"
        gym_leader_pokemon = Pokemon("Onix", "Rock", 60, ["Rock Throw", "Bind", "Tackle"])
        speak(f"{gym_leader} challenges you with {gym_leader_pokemon}!")

        player_pokemon = self.player.choose_pokemon()
        if player_pokemon:
            self.battle(player_pokemon, gym_leader_pokemon)
            if gym_leader_pokemon.is_fainted():
                self.player.badges.append("Boulder Badge")
                self.player.score += 20
                speak(f"Congratulations! You earned the Boulder Badge.")
            else:
                speak("You lost! Try again.")

    def start(self):
        speak("Welcome to the Pokémon Adventure Game!")
        name = input("Enter your name: ")
        self.player = Player(name)

        # Add starter Pokemon
        starter = Pokemon("Charmander", "Fire", 50, ["Ember", "Scratch", "Growl"])
        self.player.pokemon.append(starter)

        speak(f"Hello {self.player.name}! You received your starter Pokémon: {starter}")

        while True:
            speak("\nWhat would you like to do?")
            speak("1. Explore the wild")
            speak("2. Challenge the Gym")
            speak("3. View score and badges")
            speak("4. View Pokémon")
            speak("5. Exit game")
            choice = input("Choose an option: ")

            if choice == "1":
                self.explore_wild()
            elif choice == "2":
                self.gym_challenge()
            elif choice == "3":
                speak(f"Score: {self.player.score}")
                speak(f"Badges: {', '.join(self.player.badges) if self.player.badges else 'None'}")
            elif choice == "4":
                self.player.view_pokemon()
            elif choice == "5":
                speak("Thanks for playing!")
                break
            else:
                speak("Invalid choice. Try again.")

# Starting the game
game = Game()
game.start()
