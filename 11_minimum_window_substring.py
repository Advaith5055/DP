from collections import Counter


def minimum_window(text, target):
    needed = Counter(target)
    missing = len(target)
    left = 0
    start = 0
    length = float("inf")

    for right, char in enumerate(text):
        if needed[char] > 0:
            missing -= 1
        needed[char] -= 1

        while missing == 0:
            if right - left + 1 < length:
                start = left
                length = right - left + 1
            needed[text[left]] += 1
            if needed[text[left]] > 0:
                missing += 1
            left += 1

    return "" if length == float("inf") else text[start : start + length]


assert minimum_window("ADOBECODEBANC", "ABC") == "BANC"
assert minimum_window("a", "a") == "a"
assert minimum_window("a", "aa") == ""
