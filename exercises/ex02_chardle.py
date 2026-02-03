"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730773822"


def main() -> None:
    """Start of Chardle game"""
    contains_char(user_word_input=input_word(), user_letter_input=input_letter())


def input_word() -> str:
    """Enter 5-Character word"""
    # the length of the word must equal 5 and nothing else
    user_word_input = input("Enter a 5-character word: ")
    if len(user_word_input) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
        # exit code if the user does not put in a 5 character word
    return user_word_input


def input_letter() -> str:
    """Enter single character"""

    user_letter_input = input("Enter a single character: ")
    if len(user_letter_input) != 1:
        print("Error: Character must be a single character.")
        exit()
        # exit the code when the user does not put in one character
    return user_letter_input


def contains_char(user_word_input: str, user_letter_input: str) -> None:
    print("Searching for", user_letter_input, "in", user_word_input)
    # does the person have the correct letter
    total_characters_correct: int = 0
    if user_word_input[0] == user_letter_input:
        print(user_letter_input, "found at index 0")
        total_characters_correct = total_characters_correct + 1
    if user_word_input[1] == user_letter_input:
        print(user_letter_input, "found at index 1")
        total_characters_correct = total_characters_correct + 1
    if user_word_input[2] == user_letter_input:
        print(user_letter_input, "found at index 2")
        total_characters_correct = total_characters_correct + 1
    if user_word_input[3] == user_letter_input:
        print(user_letter_input, "found at index 3")
        total_characters_correct = total_characters_correct + 1
    if user_word_input[4] == user_letter_input:
        print(user_letter_input, "found at index 4")
        total_characters_correct = total_characters_correct + 1
    # make sure what is being printed it right
    if total_characters_correct == 0:
        print("No instances of", user_letter_input, "found in", user_word_input)
    elif total_characters_correct == 1:
        print("1 instance of", user_letter_input, "found in", user_word_input)
    else:
        print(
            total_characters_correct,
            "instances of",
            user_letter_input,
            "found in",
            user_word_input,
        )


if __name__ == "__main__":
    main()
# don't forget to call the function
