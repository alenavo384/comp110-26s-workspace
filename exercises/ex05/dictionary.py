"""Dictionary Utility Functions."""

__author__ = "730773822"


# Swapping keys and values in dictionary
def invert(my_dictionary: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values in a dictionary."""
    result: dict[str, str] = {}

    for key in my_dictionary:
        value = my_dictionary[key]

        if value in result:
            raise KeyError("Duplicate key when inverting dictionary.")

        result[value] = key

    return result


def favorite_color(name_color: dict[str, str]) -> str:
    """Return the most common favorite color."""
    number_of_color: dict[str, int] = {}

    for name in name_color:
        color = name_color[name]

        if color in number_of_color:
            number_of_color[color] += 1
        else:
            number_of_color[color] = 1

    most_common = ""
    highest_number = 0

    for color in number_of_color:
        if number_of_color[color] > highest_number:
            most_common = color
            highest_number = number_of_color[color]

    return most_common


def count(items: list[str]) -> dict[str, int]:
    """Counting things on a list."""
    result: dict[str, int] = {}

    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Group by first letter."""
    result: dict[str, list[str]] = {}

    for thing in words:
        first_letter = thing[0].lower()

        if first_letter.isalpha():
            if first_letter in result:
                result[first_letter].append(thing)
            else:
                result[first_letter] = [thing]

    return result


# if student was there that day add them to list
def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Who was there or not."""
    if day not in attendance:
        attendance[day] = [student]
    else:
        if student not in attendance[day]:
            attendance[day].append(student)
