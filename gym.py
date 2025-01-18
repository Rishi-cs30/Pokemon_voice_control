# gym.py

import random
from pokemon import Pokemon


class Gym:

    def __init__(self, name, leader, badge, leader_pokemon):
        self.name = name  # Gym name (e.g., Pewter Gym)
        self.leader = leader  # Gym leader's name
        self.badge = badge  # Badge the player will earn after defeating the gym
        self.leader_pokemon = leader_pokemon  # Gym leader's Pokémon

    def storytelling(self):
        """Display the gym's challenge introduction."""
        print(f"Welcome to the {self.name} Gym!")
        print(f"{self.leader}, the Gym Leader, challenges you!")
        print(f"{self.leader} sends out {self.leader_pokemon.name}!")

    def gym_challenge(self, player):
        """Start the gym battle and challenge the player."""
        self.storytelling()  # Show gym challenge intro
        player_pokemon = player.choose_pokemon(
        )  # Let the player choose a Pokémon
        if player_pokemon:
            self.battle(player_pokemon,
                        self.leader_pokemon)  # Start the battle
            player.remove_fainted_pokemon(
            )  # Remove fainted Pokémon after the battle
            if self.leader_pokemon.is_fainted(
            ):  # If the gym leader's Pokémon faints
                player.badges.append(self.badge)  # Player earns a badge
                player.score += 20  # Increase the player's score
                print(f"Congratulations! You earned the {self.badge}.")
                self.remove_pokemon_from_gym(
                    player)  # Remove gym leader's Pokémon
            else:
                print("You lost! Try again.")

    def battle(self, player_pokemon, gym_pokemon):
        """Simulate the battle between player's and gym leader's Pokémon."""
        while player_pokemon.health > 0 and gym_pokemon.health > 0:  # Battle continues
            print(f"{player_pokemon.name} HP: {player_pokemon.health} | "
                  f"{gym_pokemon.name} HP: {gym_pokemon.health}")
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
            ):  # Gym leader's Pokémon attacks back
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

    def remove_pokemon_from_gym(self, player):
        """Remove the defeated gym leader's Pokémon from the player's Pokémon bag."""
        if self.leader_pokemon in player.pokemon_bag:
            player.pokemon_bag.remove(self.leader_pokemon)
        print(
            f"{self.leader}'s Pokémon has been removed from your Pokémon list!"
        )
