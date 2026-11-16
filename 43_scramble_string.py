def is_scramble(first, second):
    memo = {}

    def solve(left, right):
        key = (left, right)
        if key in memo:
            return memo[key]
        if left == right:
            return True
        if sorted(left) != sorted(right):
            return False

        for split in range(1, len(left)):
            if solve(left[:split], right[:split]) and solve(left[split:], right[split:]):
                memo[key] = True
                return True
            if solve(left[:split], right[-split:]) and solve(left[split:], right[:-split]):
                memo[key] = True
                return True

        memo[key] = False
        return False

    return solve(first, second)


assert is_scramble("great", "rgeat")
assert not is_scramble("abcde", "caebd")
