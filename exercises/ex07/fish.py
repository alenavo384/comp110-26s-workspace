"""File to define Fish class."""

__author__ = "730773822"


class Fish:
    """What is happening with fish."""

    age: int

    def __init__(self) -> None:
        """Age of fish."""
        self.age = 0

    def one_day(self) -> None:
        """How many days."""
        self.age += 1
