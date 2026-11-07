def min_palindrome_cuts(text):
    size = len(text)
    if size < 2:
        return 0

    palindromes = [[False] * size for _ in range(size)]
    cuts = list(range(size))

    for end in range(size):
        for start in range(end + 1):
            if text[start] == text[end] and (end - start < 2 or palindromes[start + 1][end - 1]):
                palindromes[start][end] = True
                cuts[end] = 0 if start == 0 else min(cuts[end], cuts[start - 1] + 1)

    return cuts[-1]


assert min_palindrome_cuts("aab") == 1
assert min_palindrome_cuts("racecar") == 0
assert min_palindrome_cuts("banana") == 1
