import random
import pyttsx3
import speech_recognition as sr
from fuzzywuzzy import process

# Initialize pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Pokémon dictionary
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
    print(text)  # Print the text to the console
    engine.say(text)  # Speak the text
    engine.runAndWait()

def listen():
    """Capture voice input and return as text."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust to background noise
        speak("Listening for your response...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            speak(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
        except sr.WaitTimeoutError:
            speak("You took too long to respond.")
        return None

def match_command(user_input, options, threshold=80):
    """Match user input to the closest valid option with at least threshold% similarity."""
    if user_input:
        match, confidence = process.extractOne(user_input, options)
        if confidence >= threshold:
            return match
    return None

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
        speak("Say the number of the Pokémon you want to choose.")
        command = listen()
        try:
            choice = int(command) - 1
            if 0 <= choice < len(self.pokemon) and not self.pokemon[choice].is_fainted():
                return self.pokemon[choice]
        except (ValueError, TypeError):
            pass
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

            speak("Your moves:")
            for i, move in enumerate(player_pokemon.moves):
                speak(f"{i + 1}. {move}")
            command = listen()
            matched_move = match_command(command, player_pokemon.moves)
            if matched_move:
                damage = self.calculate_damage(player_pokemon, wild_pokemon, matched_move)
                wild_pokemon.health -= damage
                speak(f"{player_pokemon.name} used {matched_move} and dealt {damage} damage!")
            else:
                speak("Invalid move choice.")

            if wild_pokemon.is_fainted():
                speak(f"The wild {wild_pokemon.name} fainted!")
                self.player.score += 10
                break

            wild_move = random.choice(wild_pokemon.moves)
            damage = self.calculate_damage(wild_pokemon, player_pokemon, wild_move)
            player_pokemon.health -= damage
            speak(f"The wild {wild_pokemon.name} used {wild_move} and dealt {damage} damage!")

            if player_pokemon.is_fainted():
                speak(f"Your {player_pokemon.name} fainted!")
                break

        self.player.remove_fainted_pokemon()

    def explore_wild(self):
        speak("Exploring the wild...")

        wild_pokemon_name = random.choice(list(pokemon_dict.keys()))
        wild_pokemon_data = pokemon_dict[wild_pokemon_name]
        wild_pokemon = Pokemon(wild_pokemon_name, wild_pokemon_data['type'], wild_pokemon_data['health'], wild_pokemon_data['moves'])

        speak(f"A wild {wild_pokemon.name} appeared!")
        speak("Say 'catch' to catch it or 'fight' to battle it.")
        command = listen()
        matched_command = match_command(command, ["catch", "fight"])

        if matched_command == "catch":
            if random.random() < 0.5:
                speak(f"Congratulations! You caught the wild {wild_pokemon.name}!")
                self.player.pokemon.append(wild_pokemon)
            else:
                speak(f"Oh no! The wild {wild_pokemon.name} escaped!")
        elif matched_command == "fight":
            player_pokemon = self.player.choose_pokemon()
            if player_pokemon:
                self.battle(player_pokemon, wild_pokemon)
        else:
            speak("Invalid choice. The wild Pokémon ran away.")

    def start(self):
        speak("Welcome to the Pokémon Adventure Game!")
        name = input("Enter your name: ")
        self.player = Player(name)

        starter = Pokemon("Charmander", "Fire", 50, ["Ember", "Scratch", "Growl"])
        self.player.pokemon.append(starter)

        speak(f"Hello {self.player.name}! You received your starter Pokémon: {starter}")

        while True:
            speak("What would you like to do?")
            speak("Say 'explore', 'gym', 'score', 'view', or 'exit'.")
            command = listen()
            matched_command = match_command(command, ["explore", "gym", "score", "view", "exit"])

            if matched_command == "explore":
                self.explore_wild()
            elif matched_command == "gym":
                speak("Gym challenges are not implemented yet.")
            elif matched_command == "score":
                speak(f"Score: {self.player.score}")
            elif matched_command == "view":
                self.player.view_pokemon()
            elif matched_command == "exit":
                speak("Thanks for playing!")
                break
            else:
                speak("Invalid choice. Try again.")

# Start the game
game = Game()
game.start()
