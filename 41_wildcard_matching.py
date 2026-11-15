def is_match(text, pattern):
    previous = [False] * (len(pattern) + 1)
    previous[0] = True

    for j, char in enumerate(pattern, 1):
        if char == "*":
            previous[j] = previous[j - 1]

    for letter in text:
        current = [False] * (len(pattern) + 1)
        for j, char in enumerate(pattern, 1):
            if char == "*":
                current[j] = current[j - 1] or previous[j]
            elif char == "?" or char == letter:
                current[j] = previous[j - 1]
        previous = current

    return previous[-1]


assert is_match("adceb", "*a*b")
assert not is_match("acdcb", "a*c?b")
