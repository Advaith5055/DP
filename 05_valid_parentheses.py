def valid_parentheses(text: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack


if __name__ == "__main__":
    assert valid_parentheses("()")
    assert valid_parentheses("()[]{}")
    assert not valid_parentheses("(]")
    assert not valid_parentheses("([)]")
    assert valid_parentheses("{[]}")
