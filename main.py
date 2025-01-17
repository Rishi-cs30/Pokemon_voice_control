import random


# Define the Pokemon class with attributes like name, type, health, and moves
class Pokemon:

    def __init__(self, name, p_type, health, moves):
        self.name = name  # Pokemon name
        self.type = p_type  # Pokemon type (e.g., Electric, Fire)
        self.health = health  # Health points (HP)
        self.moves = moves  # List of moves the Pokemon can use

    # Method to take damage, reducing the Pokemon's health
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:  # Ensure health doesn't go below 0
            self.health = 0

    # Method to check if the Pokemon has fainted
    def is_fainted(self):
        return self.health <= 0

    # Method to heal the Pokemon by a given amount
    def heal(self, amount):
        self.health += amount

    # Method to represent the Pokemon object as a string (for easy display)
    def __str__(self):
        return f"{self.name} (Type: {self.type}, Health: {self.health}, Moves: {', '.join(self.moves)})"


# Define the Player class which represents the player in the game
class Player:

    def __init__(self):
        self.pokemon_bag = []  # List to store the player's Pokémon
        self.badges = []  # List to store the badges the player has earned
        self.score = 0  # Player's score

    # Method to add a Pokémon to the player's collection
    def add_pokemon(self, pokemon):
        if len(self.pokemon_bag) < 6:  # A player can only have 6 Pokémon
            self.pokemon_bag.append(pokemon)
        else:
            print("You can only have 6 Pokémon at a time.")

    # Method to remove fainted Pokémon from the player's collection
    def remove_fainted_pokemon(self):
        for pokemon in self.pokemon_bag[:]:  # Iterate over a copy of the list to avoid modifying it while iterating
            if pokemon.is_fainted():
                self.pokemon_bag.remove(
                    pokemon
                )  # Remove the fainted Pokémon from the player's list

    # Method to let the player choose a Pokémon for battle
    def choose_pokemon(self):
        if not self.pokemon_bag:  # Check if the player has any Pokémon
            print("You have no Pokémon available!")
            return None
        print("Choose a Pokémon:")
        # Display all the Pokémon in the player's collection
        for i, p in enumerate(self.pokemon_bag, 1):
            print(f"{i}. {p}")
        while True:
            try:
                choice = int(input("Enter the number of your choice: ")
                             ) - 1  # Input choice from the user
                if 0 <= choice < len(self.pokemon_bag):
                    return self.pokemon_bag[choice]
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

    # Method to display all the Pokémon the player currently has
    def view_pokemon(self):
        if not self.pokemon_bag:  # Check if the player has no Pokémon
            print("You have no Pokémon.")
        else:
            print("Your Pokémon:")
            for p in self.pokemon_bag:  # Display each Pokémon in the collection
                print(p)


# Define the Gym class which represents a gym in the game
class Gym:

    def __init__(self, name, leader, badge, leader_pokemon):
        self.name = name  # Gym name (e.g., Pewter Gym)
        self.leader = leader  # Gym leader's name
        self.badge = badge  # Badge the player will earn after defeating the gym
        self.leader_pokemon = leader_pokemon  # Gym leader's Pokémon

    # Method to display the gym's challenge introduction
    def storytelling(self):
        print(f"Welcome to the {self.name} Gym!")
        print(f"{self.leader}, the Gym Leader, challenges you!")
        print(f"{self.leader} sends out {self.leader_pokemon.name}!")

    # Method to start the gym battle and challenge the player
    def gym_challenge(self, player):
        self.storytelling()  # Show gym challenge intro
        player_pokemon = player.choose_pokemon(
        )  # Let the player choose a Pokémon
        if player_pokemon:
            self.battle(player_pokemon,
                        self.leader_pokemon)  # Start the battle
            if self.leader_pokemon.is_fainted(
            ):  # If the gym leader's Pokémon faints
                player.badges.append(self.badge)  # Player earns a badge
                player.score += 20  # Increase the player's score
                print(f"Congratulations! You earned the {self.badge}.")
                self.remove_pokemon_from_gym(
                    player)  # Remove gym leader's Pokémon from player's list
            else:
                print("You lost! Try again.")

    # Method to simulate the battle between player's and gym leader's Pokémon
    def battle(self, player_pokemon, gym_pokemon):
        while player_pokemon.health > 0 and gym_pokemon.health > 0:  # Battle continues until one Pokémon faints
            print(
                f"{player_pokemon.name} HP: {player_pokemon.health} | {gym_pokemon.name} HP: {gym_pokemon.health}"
            )
            move = input(
                f"Choose {player_pokemon.name}'s move ({'/'.join(player_pokemon.moves)}): "
            ).strip()
            if move in player_pokemon.moves:  # Check if the move is valid
                damage = 15  # Deal a fixed damage
                gym_pokemon.take_damage(
                    damage)  # Apply damage to the gym's Pokémon
                print(
                    f"{player_pokemon.name} used {move}! {gym_pokemon.name} took {damage} damage."
                )
            else:
                print(f"{player_pokemon.name} doesn't know that move!")

            if not gym_pokemon.is_fainted(
            ):  # Gym leader's Pokémon attacks back if it's still alive
                opponent_move = random.choice(
                    gym_pokemon.moves)  # Gym leader chooses a random move
                damage = 10  # Gym leader's Pokémon deals damage
                player_pokemon.take_damage(
                    damage)  # Apply damage to the player's Pokémon
                print(
                    f"{gym_pokemon.name} used {opponent_move}! {player_pokemon.name} took {damage} damage."
                )

        # Determine which Pokémon fainted
        if player_pokemon.is_fainted():
            print(f"{player_pokemon.name} fainted!")
        else:
            print(f"{gym_pokemon.name} fainted!")

    # Method to remove the defeated gym leader's Pokémon from the player's list
    def remove_pokemon_from_gym(self, player):
        """Remove the defeated gym leader's Pokémon from the player's Pokémon bag."""
        if self.leader_pokemon in player.pokemon_bag:
            player.pokemon_bag.remove(self.leader_pokemon)
        print(
            f"{self.leader}'s Pokémon has been removed from your Pokémon list!"
        )


# Main Game class that handles the entire gameplay
class Game:

    def __init__(self):
        self.player = Player()  # Create a new player
        self.pokemon_dict = {  # Dictionary of Pokémon with their stats
            'Pikachu': {
                'type': 'Electric',
                'health': 35,
                'moves': ['Thunder Shock', 'Quick Attack']
            },
            'Charmander': {
                'type': 'Fire',
                'health': 39,
                'moves': ['Ember', 'Scratch']
            },
            'Bulbasaur': {
                'type': 'Grass',
                'health': 45,
                'moves': ['Vine Whip', 'Tackle']
            },
            'Squirtle': {
                'type': 'Water',
                'health': 44,
                'moves': ['Water Gun', 'Tackle']
            },
            'Eevee': {
                'type': 'Normal',
                'health': 55,
                'moves': ['Tackle', 'Quick Attack']
            },
            'Jigglypuff': {
                'type': 'Fairy',
                'health': 115,
                'moves': ['Sing', 'Pound']
            },
        }
        self.gyms = [  # List of gym challenges
            Gym("Pewter Gym", "Brock", "Boulder Badge",
                Pokemon("Onix", "Rock", 60, ["Rock Throw", "Tackle"])),
            Gym("Cerulean Gym", "Misty", "Cascade Badge",
                Pokemon("Starmie", "Water", 70, ["Water Gun", "Tackle"])),
            Gym(
                "Vermilion Gym", "Lt. Surge", "Thunder Badge",
                Pokemon("Raichu", "Electric", 80,
                        ["Thunderbolt", "Quick Attack"])),
        ]

    # Introductory storytelling before starting the game
    def storytelling_intro(self):
        print("Welcome to the world of Pokémon!")
        print(
            "You are about to embark on an exciting journey to become a Pokémon master!"
        )
        print("Choose your starter Pokémon and begin your adventure!")

    # Method to let the player choose a starter Pokémon
    def choose_starter_pokemon(self):
        starters = random.sample(list(self.pokemon_dict.keys()),
                                 3)  # Randomly pick 3 starter Pokémon
        print("Choose your starter Pokémon:")
        for i, name in enumerate(starters, 1):
            print(f"{i}. {name}")
        while True:
            try:
                choice = int(input("Enter the number of your choice: ")) - 1
                if 0 <= choice < len(starters):
                    chosen_name = starters[choice]
                    stats = self.pokemon_dict[chosen_name]
                    starter_pokemon = Pokemon(chosen_name, stats['type'],
                                              stats['health'], stats['moves'])
                    self.player.add_pokemon(
                        starter_pokemon
                    )  # Add the chosen Pokémon to the player's bag
                    print(f"You chose {starter_pokemon.name}!")
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

    # Method to simulate exploring the wild to find wild Pokémon
    def explore_wild(self):
        print("Exploring the wild...")
        wild_pokemon_name = random.choice(list(
            self.pokemon_dict.keys()))  # Randomly pick a wild Pokémon
        wild_pokemon_stats = self.pokemon_dict[wild_pokemon_name]
        wild_pokemon = Pokemon(wild_pokemon_name, wild_pokemon_stats['type'],
                               wild_pokemon_stats['health'],
                               wild_pokemon_stats['moves'])
        print(f"You encountered a wild {wild_pokemon.name}!")
        print("1. Fight\n2. Catch")
        choice = input("Choose an option: ").strip()

        if choice == '1':  # Fight option
            player_pokemon = self.player.choose_pokemon(
            )  # Let the player choose a Pokémon to fight with
            if player_pokemon:
                print(
                    f"A battle between {player_pokemon.name} and {wild_pokemon.name} begins!"
                )
                while player_pokemon.health > 0 and wild_pokemon.health > 0:
                    print(
                        f"{player_pokemon.name} HP: {player_pokemon.health} | {wild_pokemon.name} HP: {wild_pokemon.health}"
                    )
                    move = input(
                        f"Choose {player_pokemon.name}'s move ({'/'.join(player_pokemon.moves)}): "
                    ).strip()
                    if move in player_pokemon.moves:
                        damage = 15
                        wild_pokemon.take_damage(
                            damage)  # Apply damage to the wild Pokémon
                        print(
                            f"{player_pokemon.name} used {move}! {wild_pokemon.name} took {damage} damage."
                        )
                    else:
                        print(f"{player_pokemon.name} doesn't know that move!")

                    if wild_pokemon.health > 0:
                        opponent_move = random.choice(wild_pokemon.moves)
                        damage = 10
                        player_pokemon.take_damage(
                            damage)  # Wild Pokémon attacks back
                        print(
                            f"{wild_pokemon.name} used {opponent_move}! {player_pokemon.name} took {damage} damage."
                        )

                # Determine the battle outcome
                if player_pokemon.is_fainted():
                    print(
                        f"{player_pokemon.name} fainted!\n Your Pokemon is sent to the Pokemon Center."
                    )
                    self.player.remove_fainted_pokemon(
                    )  # Remove fainted Pokémon from the player's collection
                    print("You lost the fight. Returning to the main menu.")
                else:
                    print(f"{wild_pokemon.name} fainted!")
                    self.player.score += 10  # Increase the player's score for winning the fight
                    print("You won the fight!")
                input("Press Enter to return to the main menu.")

        elif choice == '2':  # Catch option
            if random.random() <= 0.8:  # 80% chance to catch the wild Pokémon
                self.player.add_pokemon(
                    wild_pokemon
                )  # Add the wild Pokémon to the player's collection
                print(f"You caught a wild {wild_pokemon.name}!")
            else:
                print(f"{wild_pokemon.name} escaped!")
            input("Press Enter to return to the main menu.")
        else:
            print("Invalid option. Returning to main menu.")

    # Method to display the main menu options
    def display_menu(self):
        print("\nMain Menu:")
        print("1. Explore Wild")
        print("2. Gym Challenge")
        print("3. View Pokémon")
        print("4. View High Scores")
        print("5. Exit Game")

    # Main method to start the game and manage gameplay flow
    def start_game(self):
        self.storytelling_intro()  # Display the intro
        self.choose_starter_pokemon(
        )  # Let the player choose a starter Pokémon
        while True:
            # Check if all gyms are defeated
            if not self.gyms:  # If there are no more gyms left (i.e., all gyms are defeated)
                self.display_winning_scene()  # Display the winning scene
                break

            self.display_menu()  # Show main menu
            choice = input("Choose an option: ").strip()
            if choice == '1':
                self.explore_wild()  # Explore the wild
            elif choice == '2':
                for i, gym in enumerate(self.gyms, 1):
                    print(f"{i}. {gym.name}")
                try:
                    gym_choice = int(input("Choose a gym: ")) - 1
                    if 0 <= gym_choice < len(self.gyms):
                        self.gyms[gym_choice].gym_challenge(
                            self.player)  # Challenge the gym
                        if self.gyms[gym_choice].leader_pokemon.is_fainted(
                        ):  # Gym defeated
                            del self.gyms[
                                gym_choice]  # Remove the defeated gym from the list
                            print(
                                "Congratulations! You defeated the gym leader!"
                            )
                except ValueError:
                    print("Invalid input. Enter a number.")
            elif choice == '3':
                self.player.view_pokemon()  # View the player's Pokémon
            elif choice == '4':
                print(f"Your score: {self.player.score}")
                print(
                    f"Badges earned: {', '.join(self.player.badges) if self.player.badges else 'None'}"
                )
            elif choice == '5':
                print("Exiting game. Goodbye!")  # Exit the game
                break
            else:
                print("Invalid choice. Try again.")

    # Method to display the winning screen when the player has earned all badges
    def display_winning_scene(self):
        print("\n🎉🎉 CONGRATULATIONS! 🎉🎉")
        print("You have defeated all Gym Leaders and earned all the badges!")
        print("You are now a Pokémon Champion!")
        print("\n🏆 Final Score: ", self.player.score)
        print("🏅 Badges Collected: ", ", ".join(self.player.badges))
        print("🐾 Remaining Pokémon:")
        for pokemon in self.player.pokemon_bag:  # Display the Pokémon the player still has
            print(pokemon)
        print("\nThank you for playing!")


# Run the game if this file is executed as the main program
if __name__ == "__main__":
    game = Game()
    game.start_game()
