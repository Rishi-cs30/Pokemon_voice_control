import random

class Pokemon:
    def __init__(self, name, p_type, health, moves):
        self.name = name
        self.type = p_type
        self.health = health
        self.moves = moves

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_fainted(self):
        return self.health <= 0

    def heal(self, amount):
        self.health += amount

    def __str__(self):
        return f"{self.name} (Type: {self.type}, Health: {self.health}, Moves: {', '.join(self.moves)})"

class Player:
    def __init__(self):
        self.pokemon_bag = []
        self.badges = []
        self.score = 0

    def add_pokemon(self, pokemon):
        if len(self.pokemon_bag) < 6:
            self.pokemon_bag.append(pokemon)
        else:
            print("You can only have 6 Pokémon at a time.")

    def remove_fainted_pokemon(self):
        self.pokemon_bag = [p for p in self.pokemon_bag if not p.is_fainted()]

    def choose_pokemon(self):
        if not self.pokemon_bag:
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
        if not self.pokemon_bag:
            print("You have no Pokémon.")
        else:
            print("Your Pokémon:")
            for p in self.pokemon_bag:
                print(p)



class Gym:
    def __init__(self, name, leader, badge, leader_pokemon):
        self.name = name
        self.leader = leader
        self.badge = badge
        self.leader_pokemon = leader_pokemon

    def storytelling(self):
        print(f"Welcome to the {self.name} Gym!")
        print(f"{self.leader}, the Gym Leader, challenges you!")
        print(f"{self.leader} sends out {self.leader_pokemon.name}!")

    def gym_challenge(self, player):
        self.storytelling()
        player_pokemon = player.choose_pokemon()
        if player_pokemon:
            self.battle(player_pokemon, self.leader_pokemon)
            if self.leader_pokemon.is_fainted():
                player.badges.append(self.badge)
                player.score += 20
                print(f"Congratulations! You earned the {self.badge}.")
            else:
                print("You lost! Try again.")

    def battle(self, player_pokemon, gym_pokemon):
        while player_pokemon.health > 0 and gym_pokemon.health > 0:
            print(f"{player_pokemon.name} HP: {player_pokemon.health} | {gym_pokemon.name} HP: {gym_pokemon.health}")
            move = input(f"Choose {player_pokemon.name}'s move ({'/'.join(player_pokemon.moves)}): ").strip()
            if move in player_pokemon.moves:
                damage = 15
                gym_pokemon.take_damage(damage)
                print(f"{player_pokemon.name} used {move}! {gym_pokemon.name} took {damage} damage.")
            else:
                print(f"{player_pokemon.name} doesn't know that move!")

            if not gym_pokemon.is_fainted():
                opponent_move = random.choice(gym_pokemon.moves)
                damage = 10
                player_pokemon.take_damage(damage)
                print(f"{gym_pokemon.name} used {opponent_move}! {player_pokemon.name} took {damage} damage.")

        if player_pokemon.is_fainted():
            print(f"{player_pokemon.name} fainted!")
        else:
            print(f"{gym_pokemon.name} fainted!")

class Game:
    def __init__(self):
        self.player = Player()
        self.pokemon_dict = {
            'Pikachu': {'type': 'Electric', 'health': 35, 'moves': ['Thunder Shock', 'Quick Attack']},
            'Charmander': {'type': 'Fire', 'health': 39, 'moves': ['Ember', 'Scratch']},
            'Bulbasaur': {'type': 'Grass', 'health': 45, 'moves': ['Vine Whip', 'Tackle']},
            'Squirtle': {'type': 'Water', 'health': 44, 'moves': ['Water Gun', 'Tackle']},
            'Eevee': {'type': 'Normal', 'health': 55, 'moves': ['Tackle', 'Quick Attack']},
            'Jigglypuff': {'type': 'Fairy', 'health': 115, 'moves': ['Sing', 'Pound']},
        }
        self.gyms = [
            Gym("Pewter Gym", "Brock", "Boulder Badge", Pokemon("Onix", "Rock", 60, ["Rock Throw", "Tackle"])),
            Gym("Cerulean Gym", "Misty", "Cascade Badge", Pokemon("Starmie", "Water", 70, ["Water Gun", "Tackle"])),
            Gym("Vermilion Gym", "Lt. Surge", "Thunder Badge", Pokemon("Raichu", "Electric", 80, ["Thunderbolt", "Quick Attack"])),
        ]

    def storytelling_intro(self):
        print("Welcome to the world of Pokémon!")
        print("You are about to embark on an exciting journey to become a Pokémon master!")
        print("Choose your starter Pokémon and begin your adventure!")

    def choose_starter_pokemon(self):
        starters = random.sample(list(self.pokemon_dict.keys()), 3)
        print("Choose your starter Pokémon:")
        for i, name in enumerate(starters, 1):
            print(f"{i}. {name}")
        while True:
            try:
                choice = int(input("Enter the number of your choice: ")) - 1
                if 0 <= choice < len(starters):
                    chosen_name = starters[choice]
                    stats = self.pokemon_dict[chosen_name]
                    starter_pokemon = Pokemon(chosen_name, stats['type'], stats['health'], stats['moves'])
                    self.player.add_pokemon(starter_pokemon)
                    print(f"You chose {starter_pokemon.name}!")
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

    def explore_wild(self):
        print("Exploring the wild...")
        wild_pokemon_name = random.choice(list(self.pokemon_dict.keys()))
        wild_pokemon_stats = self.pokemon_dict[wild_pokemon_name]
        wild_pokemon = Pokemon(wild_pokemon_name, wild_pokemon_stats['type'], wild_pokemon_stats['health'], wild_pokemon_stats['moves'])
        print(f"You encountered a wild {wild_pokemon.name}!")
        print(f"1. Fight\n2. Catch")
        choice = input("Choose an option: ").strip()

        if choice == '1':  # Fight
            player_pokemon = self.player.choose_pokemon()
            if player_pokemon:
                print(f"A battle between {player_pokemon.name} and {wild_pokemon.name} begins!")
                while player_pokemon.health > 0 and wild_pokemon.health > 0:
                    print(f"{player_pokemon.name} HP: {player_pokemon.health} | {wild_pokemon.name} HP: {wild_pokemon.health}")
                    move = input(f"Choose {player_pokemon.name}'s move ({'/'.join(player_pokemon.moves)}): ").strip()
                    if move in player_pokemon.moves:
                        damage = 15
                        wild_pokemon.take_damage(damage)
                        print(f"{player_pokemon.name} used {move}! {wild_pokemon.name} took {damage} damage.")
                    else:
                        print(f"{player_pokemon.name} doesn't know that move!")

                    if wild_pokemon.health > 0:
                        opponent_move = random.choice(wild_pokemon.moves)
                        damage = 10
                        player_pokemon.take_damage(damage)
                        print(f"{wild_pokemon.name} used {opponent_move}! {player_pokemon.name} took {damage} damage.")

                if player_pokemon.is_fainted():
                    print(f"{player_pokemon.name} fainted!")
                    self.player.remove_fainted_pokemon()  # Remove fainted Pokémon
                    print("You lost the fight. Returning to the main menu.")
                else:
                    print(f"{wild_pokemon.name} fainted!")
                    self.player.score += 10
                    print("You won the fight!")
                input("Press Enter to return to the main menu.")

        elif choice == '2':  # Catch
            self.player.add_pokemon(wild_pokemon)
            print(f"You caught a wild {wild_pokemon.name}!")
            input("Press Enter to return to the main menu.")

        else:
            print("Invalid option. Returning to main menu.")

    def display_menu(self):
        print("\nMain Menu:")
        print("1. Explore Wild")
        print("2. Gym Challenge")
        print("3. View Pokémon")
        print("4. View High Scores")
        print("5. Exit Game")

    def start_game(self):
        self.storytelling_intro()
        self.choose_starter_pokemon()
        while True:
            self.display_menu()
            choice = input("Choose an option: ").strip()
            if choice == '1':
                self.explore_wild()
            elif choice == '2':
                for i, gym in enumerate(self.gyms, 1):
                    print(f"{i}. {gym.name}")
                gym_choice = int(input("Choose a gym: ")) - 1
                if 0 <= gym_choice < len(self.gyms):
                    self.gyms[gym_choice].gym_challenge(self.player)
            elif choice == '3':
                self.player.view_pokemon()
            elif choice == '4':
                print(f"Your score: {self.player.score}")
                print(f"Badges earned: {', '.join(self.player.badges) if self.player.badges else 'None'}")
            elif choice == '5':
                print("Exiting game. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    game = Game()
    game.start_game()
