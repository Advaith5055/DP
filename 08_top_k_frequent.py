def top_k_frequent(numbers: list[int], count: int) -> list[int]:
    frequencies = {}

    for number in numbers:
        frequencies[number] = frequencies.get(number, 0) + 1

    return [number for number, _ in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)[:count]]


if __name__ == "__main__":
    assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_frequent([4, 4, 5, 6, 6, 6], 1) == [6]
