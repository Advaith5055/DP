def minimum_window_subsequence(text, target):
    width = len(target)
    starts = [-1] * width
    best = ""

    for index, char in enumerate(text):
        for position in range(width - 1, -1, -1):
            if char == target[position]:
                if position == 0:
                    starts[position] = index
                elif starts[position - 1] != -1:
                    starts[position] = starts[position - 1]

        if starts[-1] != -1:
            window = text[starts[-1]:index + 1]
            if not best or len(window) < len(best):
                best = window

    return best


assert minimum_window_subsequence("abcdebdde", "bde") == "bcde"
assert minimum_window_subsequence("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u") == ""
