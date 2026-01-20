"""__Tea Party__"""

__author__: str = "730773822"


def main_planner(guests: int) -> None:
    """party planner"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    "number of tea bags needed"
    return people * 2


def treats(people: int) -> int:
    """number of treats"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """total coast of tea bags and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
