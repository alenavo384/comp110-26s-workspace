"""Dictionary Unit Test."""

__author__ = "730773822"

from exercises.ex05.dictionary import invert
import pytest
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


def test_invert_a_pair() -> None:
    """Testing invert with a key-value pair."""
    assert invert({"soccer": "ball"}) == {"ball": "soccer"}


def test_invert_various_pairs() -> None:
    """Testing invert with various key-value pairs."""
    assert invert({"yes": "no", "tall": "short", "strong": "weak"}) == {
        "no": "yes",
        "short": "tall",
        "weak": "strong",
    }


def test_invert_keyerror() -> None:
    """Testing if inverting raises a KeyError on duplicate values."""
    with pytest.raises(KeyError):
        invert({"micheal": "wilson", "caleb": "wilson"})


def test_favorite_color_for_one() -> None:
    """Testing favorite_color for one entry."""
    assert favorite_color({"Alena": "Blue"}) == "blue"


def test_favorite_color_with_tie() -> None:
    """Testing favorite_color with a tie of favorite color."""
    assert favorite_color({"alena": "blue", "bob": "green"}) == "blue"


def test_favorite_color_with_no_tie() -> None:
    """Testing favorite_color for entries and no ties."""
    assert favorite_color({"alena": "blue", "bob": "green", "john": "blue"}) == "blue"


def test_count_repeated_items() -> None:
    """Testing counting with repeated values."""
    assert count(["ball", "apple", "ball"]) == {"ball": 2, "apple": 1}


def test_count_empty() -> None:
    """Testing count when the list is empty."""
    assert count([]) == {}


def test_count_one_item() -> None:
    """Testing counting with one item."""
    assert count(["dog"]) == {"dog": 1}


def test_alphabetizer_first_letter() -> None:
    """Testing alphabetizer using first letter."""
    assert alphabetizer(["alena", "ashley", "bob", "bill"]) == {
        "a": ["alena", "ashley"],
        "b": ["bob", "bill"],
    }


def test_alphabetizer_with_number() -> None:
    """Testing alphabetizer with numbers."""
    assert alphabetizer(["soccer", "123", "ball"]) == {"s": ["soccer"], "b": ["ball"]}


def test_alphabetizer_empty_list() -> None:
    """Testing alphabetizer with an empty list."""
    assert alphabetizer([]) == {}


def test_update_attendance_new_day() -> None:
    """Testing update_attendance creating a new day."""
    attendance_list = {"Monday": ["alena", "ashley"]}
    update_attendance(attendance_list, "Thursday", "ashley")
    assert attendance_list == {"Monday": ["alena", "ashley"], "Thursday": ["ashley"]}


def test_update_attendance_current_day() -> None:
    """Testting update_attendance for current day."""
    attendance_list = {"Monday": ["alena", "ashley"], "Tuesday": ["alena"]}
    update_attendance(attendance_list, "Tuesday", "alena")
    assert attendance_list == {"Monday": ["alena", "ashley"], "Tuesday": ["alena"]}


def test_update_attendance_return_method() -> None:
    """Testing update_attendance for return method to none."""
    attendance_list = {"Monday": ["alena"]}
    result = update_attendance(attendance_list, "Monday", "ashley")
    assert result is None
