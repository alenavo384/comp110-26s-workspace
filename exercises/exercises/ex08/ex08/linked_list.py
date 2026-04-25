from __future__ import annotations

__author__ = "730773822"


class Node:
    """Node in a singly-linked list recursive structure."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initialize a Node for value and next."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """REturn string with Node's values"""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Return the value of Node stored at a given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # base case when index is reached
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return maximum value in list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        # base case for last node
        return head.value
    max_rest = max(head.next)
    # start of recursive case
    if head.value > max_rest:
        return head.value
    else:
        return max_rest


def linkify(items: list[int]) -> Node | None:
    """Return linked list of nodes into list."""
    # base case
    if len(items) == 0:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return new linked list scaled by the factor."""
    # base case
    if head is None:
        return None
    # creating new node with factored scale
    return Node(head.value * factor, scale(head.next, factor))


courses: Node = Node(110, Node(210, Node(211, None)))
print(courses)
