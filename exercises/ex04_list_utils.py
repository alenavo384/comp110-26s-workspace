"""List Utility Functions"""

__author__ = "730773822"


def all(nums: list[int], target: int) -> bool:
    if len(nums) == 0:
        return False
    j = 0
    while j < len(nums):
        if nums[j] != target:
            return False
        j = j + 1
    return True


# what is the largest number in the list
def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    largest_num = input[0]
    i = 1

    while i < len(input):
        if input[i] > largest_num:
            largest_num = input[i]
        i = i + 1

    return largest_num


# making sure the list are equal in indexes
def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    if len(list_one) != len(list_two):
        return False

    i = 0
    while i < len(list_one):
        if list_one[i] != list_two[i]:
            return False
        i = i + 1
    return True


# adding to the list
def extend(list1: list[int], list2: list[int]) -> None:
    index = 0
    while index < len(list2):
        list1.append(list2[index])
        index = index + 1
