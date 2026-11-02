def can_partition(nums):
    total = sum(nums)
    if total % 2:
        return False

    target = total // 2
    possible = {0}
    for num in nums:
        possible |= {current + num for current in possible if current + num <= target}
    return target in possible


assert can_partition([1, 5, 11, 5])
assert not can_partition([1, 2, 3, 5])
