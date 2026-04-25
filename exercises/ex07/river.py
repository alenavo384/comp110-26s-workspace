"""File to define River class."""

from __future__ import annotations
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730773822"


class River:
    """River with both fish and bears."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def one_river_week(self) -> None:
        """One week in the river."""
        for _ in range(7):
            self.one_river_day()

    def check_ages(self) -> None:
        """Removing fish older than 3 and bears older than 5."""
        new_fish: list[Fish] = []
        new_bears: list[Bear] = []

        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)

        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)

        self.fish = new_fish
        self.bears = new_bears

    def remove_fish(self, amount: int) -> None:
        """Removing fish."""
        for _ in range(amount):
            if len(self.fish) > 0:
                self.fish.pop

    def bears_eating(self) -> None:
        """Bears eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self) -> None:
        """Remove bears."""
        alive_bears: list[Bear] = []

        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)

        self.bears = alive_bears

    def repopulate_fish(self) -> None:
        """Add 4 new fish."""
        num_new_fish: int = (len(self.fish) // 2) * 4

        for _ in range(num_new_fish):
            self.fish.append(Fish())

    def repopulate_bears(self) -> None:
        """Adding a new bear."""
        num_new_bears: int = len(self.bears) // 2

        for _ in range(num_new_bears):
            self.bears.append(Bear())

    def __str__(self) -> str:
        """Return string for river."""
        return (
            f"~~~ Day {self.day}: ~~~\n"
            f"Fish population: {len(self.fish)}\n"
            f"Bear population: {len(self.bears)}"
        )

    def __add__(self, other_riv: River) -> River:
        """Combinging two rivers"""
        total_fish = len(self.fish) + len(other_riv.fish)
        total_bears = len(self.bears) + len(other_riv.bears)
        return River(total_fish, total_bears)

    def __mul__(self, factor: int) -> River:
        """Returning new scale by a facotr."""
        total_fish = len(self.fish) * factor
        total_bears = len(self.bears) * factor
        return River(total_fish, total_bears)

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        print(self)
