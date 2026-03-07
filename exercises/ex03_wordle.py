"""Wordle"""

__author__ = "730773822"


def input_guess(secret_word_len: int) -> str:
    # what is the length of the secret word
    """Guess the correct length"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
        # if the length doesn't equal secret word length, its wrong
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Returning true if char_guess is found or False otherwise"""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False
    # does the letter appear in another place


WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"
# random codes for the color boxes


def emojified(guess: str, secret_word_emoji: str) -> str:
    """colored boxes representing how players guess compares to secret"""
    assert len(guess) == len(secret_word_emoji)
    result: str = ""
    index: int = 0

    while index < len(secret_word_emoji):
        if guess[index] == secret_word_emoji[index]:
            result += GREEN_BOX
        elif contains_char(secret_word=secret_word_emoji, char_guess=guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
        # Puts a green box if you got a letter in the right place
        # Puts a yellow box if you have a letter but not in the right place
        # Puts white box if nothing matches

    return result


def main(secret: str) -> None:
    """Start of wordle game/loop"""
    turn: int = 1
    won: bool = False

    while turn <= 6 and not won:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(secret_word_len=len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            won = True
        else:
            turn += 1
            # everytime someone guesses it will add one to a turn

    if won:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
    # calling the function
