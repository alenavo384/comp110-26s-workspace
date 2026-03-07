"""Dictionary Utility Functions"""

__author__ = "730773822"


# Swapping keys and values in dictionary
def invert(my_dictionary: dict[str, str]) -> dict[str, str]:
    result: dict[str, str] = {}

    for key in my_dictionary:
        value = my_dictionary[key]

        if value in result:
            raise KeyError("Duplicate key when inverting dictionary")

        result[value] = key

    return result


"""What someones favorite color is"""


def favorite_color(name_color: dict[str, str]) -> str:
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


"""Counting things on a list"""


def count(items: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}

    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


"""Group by first letter"""


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}

    for thing in words:
        first_letter = thing[0].lower()

        if first_letter.isalpha():
            if first_letter in result:
                result[first_letter].append(thing)
            else:
                result[first_letter] = [thing]

    return result


"""Who was there or not"""


# if student was there that day add them to list
def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]
