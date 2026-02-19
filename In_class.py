def check_first_letter(word: str, letter: str) -> str:
    "See if letter's value isn't one"
    if len(letter) != 1:
        return "letter's argument should be one character!"
    elif word[0] == letter:
        return "match!"
    else:
        return "no match!"


age: int = 4

"""Generating a list"""
my_numbers: list[float] = []
print(my_numbers)
my_numbers.append(1.5)
my_numbers.append(3.2)
