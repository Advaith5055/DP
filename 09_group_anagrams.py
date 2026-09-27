def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}

    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)

    return list(groups.values())


if __name__ == "__main__":
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert group_anagrams([""]) == [[""]]
