# game.py

import random
from player import Player
from gym import Gym
from pokemon import Pokemon


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
            'Meowth': {
                'type': 'Normal',
                'health': 40,
                'moves': ['Scratch', 'Bite']
            },
            'Psyduck': {
                'type': 'Water',
                'health': 50,
                'moves': ['Water Gun', 'Confusion']
            },
            'Magikarp': {
                'type': 'Water',
                'health': 20,
                'moves': ['Splash', 'Tackle']
            },
            'Gengar': {
                'type': 'Ghost/Poison',
                'health': 60,
                'moves': ['Lick', 'Shadow Ball']
            }
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

    def storytelling_intro(self):
        """Introductory storytelling before starting the game."""
        print("Welcome to the world of Pokémon!")
        print(
            "You are about to embark on an exciting journey to become a Pokémon master!"
        )
        print("Choose your starter Pokémon and begin your adventure!")

    def choose_starter_pokemon(self):
        """Let the player choose a starter Pokémon."""
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

    def explore_wild(self):
        """Simulate exploring the wild to find wild Pokémon."""
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
                        f"{player_pokemon.name} HP: {player_pokemon.health} | "
                        f"{wild_pokemon.name} HP: {wild_pokemon.health}")
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
                        f"{player_pokemon.name} fainted!\nYour Pokémon is sent to the Pokémon Center."
                    )
                    self.player.remove_fainted_pokemon(
                    )  # Remove fainted Pokémon
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

    def display_menu(self):
        """Display the main menu options."""
        print("\nMain Menu:")
        print("1. Explore Wild")
        print("2. Gym Challenge")
        print("3. View Pokémon")
        print("4. View High Scores")
        print("5. Exit Game")

    def start_game(self):
        """Main method to start the game and manage gameplay flow."""
        self.storytelling_intro()  # Display the intro
        self.choose_starter_pokemon(
        )  # Let the player choose a starter Pokémon
        while True:
            if not self.gyms:  # If there are no more gyms left
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
                                gym_choice]  # Remove the defeated gym
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

    def display_winning_scene(self):
        """Display the winning screen when the player has earned all badges."""
        print("\n🎉🎉 CONGRATULATIONS! 🎉🎉")
        print("You have defeated all Gym Leaders and earned all the badges!")
        print("You are now a Pokémon Champion!")
        print("\n🏆 Final Score: ", self.player.score)
        print("🏅 Badges Collected: ", ", ".join(self.player.badges))
        print("🐾 Remaining Pokémon:")
        for pokemon in self.player.pokemon_bag:  # Display remaining Pokémon
            print(pokemon)
        print("\nThank you for playing!")
