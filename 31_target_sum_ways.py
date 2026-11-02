def target_sum_ways(nums, target):
    ways = {0: 1}
    for num in nums:
        next_ways = {}
        for total, count in ways.items():
            next_ways[total + num] = next_ways.get(total + num, 0) + count
            next_ways[total - num] = next_ways.get(total - num, 0) + count
        ways = next_ways
    return ways.get(target, 0)


assert target_sum_ways([1, 1, 1, 1, 1], 3) == 5
assert target_sum_ways([1], 1) == 1
assert target_sum_ways([2, 3, 5], 0) == 2
