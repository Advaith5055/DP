# DSA Question 1: Linear Search

# Given a list of integers and a target value, return the index of the
# target. Return -1 when the target does not exist in the list.


def linear_search(numbers: list[int], target: int) -> int:
    """Return the index of target, or -1 if target is not present."""
    # Visit each element once and compare it with the target.
    for index, number in enumerate(numbers):
        if number == target:
            return index

    return -1


# Time complexity: O(n), because we may inspect every element.
# Space complexity: O(1), because no extra collection is created.

if __name__ == "__main__":
    assert linear_search([4, 2, 7, 1], 7) == 2
    assert linear_search([4, 2, 7, 1], 9) == -1
    assert linear_search([], 5) == -1
    print("All linear search tests passed.")
