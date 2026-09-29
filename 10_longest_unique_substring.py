def longest_unique_substring(text):
    seen = {}
    left = 0
    longest = 0

    for right, char in enumerate(text):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        longest = max(longest, right - left + 1)

    return longest


assert longest_unique_substring("abcabcbb") == 3
assert longest_unique_substring("bbbbb") == 1
assert longest_unique_substring("pwwkew") == 3
