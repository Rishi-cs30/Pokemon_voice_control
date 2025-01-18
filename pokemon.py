

class Pokemon:

    def __init__(self, name, p_type, health, moves):
        self.name = name  # Pokemon name
        self.type = p_type  # Pokemon type (e.g., Electric, Fire)
        self.health = health  # Health points (HP)
        self.moves = moves  # List of moves the Pokemon can use

    def take_damage(self, amount):
        """Reduce the Pokemon's health by the damage amount."""
        self.health -= amount
        if self.health < 0:  # Ensure health doesn't go below 0
            self.health = 0

    def is_fainted(self):
        """Check if the Pokemon has fainted."""
        return self.health <= 0

    def heal(self, amount):
        """Heal the Pokemon by a given amount."""
        self.health += amount

    def __str__(self):
        """Return a string representation of the Pokemon object."""
        return (f"{self.name} (Type: {self.type}, Health: {self.health}, "
                f"Moves: {', '.join(self.moves)})")
