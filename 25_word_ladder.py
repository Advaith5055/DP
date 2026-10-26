def ladder_length(begin_word, end_word, word_list):
    words = set(word_list)
    if end_word not in words:
        return 0

    queue = [(begin_word, 1)]
    seen = {begin_word}

    while queue:
        word, steps = queue.pop(0)
        if word == end_word:
            return steps

        for index in range(len(word)):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                next_word = word[:index] + letter + word[index + 1:]
                if next_word in words and next_word not in seen:
                    seen.add(next_word)
                    queue.append((next_word, steps + 1))

    return 0


assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
