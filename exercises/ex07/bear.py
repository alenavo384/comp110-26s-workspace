"""File to define Bear class."""

__author__ = "730773822"


class Bear:
    """What is happening with bears."""

    def __init__(self) -> None:
        """Age of bear."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """How many days."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """How many fish was ate."""
        self.hunger_score += num_fish
