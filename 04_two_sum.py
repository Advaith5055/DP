# DSA Question 4: Two Sum

# Given a list of integers and a target value, return the indices of the two
# numbers that add up to the target. Assume exactly one valid answer exists.


def two_sum(numbers: list[int], target: int) -> tuple[int, int]:
    """Return the indices of the two numbers whose sum equals target."""
    seen: dict[int, int] = {}

    for index, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return (seen[complement], index)
        seen[number] = index

    raise ValueError("No valid two-sum pair exists")


# Time complexity: O(n), because each number is processed once on average.
# Space complexity: O(n), because the hash map can store every seen number.


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    assert two_sum([3, 3], 6) == (0, 1)
    print("All two sum tests passed.")
