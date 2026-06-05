# DSA Question 2: Find the Maximum Element
#
# Given a non-empty list of integers, find and return its largest element.
# Solve the problem without using Python's built-in max() function.
#
# Example:
# numbers = [3, 8, 2, 5]
# Answer: 8


def find_maximum(numbers: list[int]) -> int:
    """Return the largest integer in a non-empty list."""
    if not numbers:
        raise ValueError("numbers must not be empty")

    largest = numbers[0]

    # Compare every remaining element with the largest value seen so far.
    for number in numbers[1:]:
        if number > largest:
            largest = number

    return largest


# Time complexity: O(n), because every element is checked once.
# Space complexity: O(1), because only one extra variable is used.

if __name__ == "__main__":
    assert find_maximum([3, 8, 2, 5]) == 8
    assert find_maximum([-4, -2, -9]) == -2
    assert find_maximum([6]) == 6
    print("All maximum element tests passed.")
