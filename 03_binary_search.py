# DSA Question 3: Binary Search

# Given a sorted list of integers and a target value, return the index of the
# target. Return -1 when the target does not exist in the list.
# The input list must be sorted in non-decreasing order.


def binary_search(numbers: list[int], target: int) -> int:
    """Return the index of target in a sorted list, or -1 if missing."""
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if numbers[mid] == target:
            return mid
        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Time complexity: O(log n), because the search space is halved each step.
# Space complexity: O(1), because the algorithm uses a constant amount of extra space.

if __name__ == "__main__":
    assert binary_search([1, 3, 5, 7, 9, 11], 7) == 3
    assert binary_search([1, 3, 5, 7, 9, 11], 1) == 0
    assert binary_search([1, 3, 5, 7, 9, 11], 12) == -1
    assert binary_search([], 4) == -1
    print("All binary search tests passed.")
