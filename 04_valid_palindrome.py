# DSA Question 4: Valid Palindrome
#
# Given a string, return True if it reads the same forward and backward
# after ignoring spaces, punctuation, and letter case. Otherwise return False.
#
# Example:
# text = "A man, a plan, a canal: Panama"
# Answer: True


def is_palindrome(text: str) -> bool:
    """Return whether text is a palindrome after normalizing characters."""
    left = 0
    right = len(text) - 1

    # Move inward from both ends, comparing only letters and digits.
    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1

        if text[left].lower() != text[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Time complexity: O(n), because each character is considered at most once.
# Space complexity: O(1), because the algorithm uses only two pointers.

if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome("No 'x' in Nixon") is True
    assert is_palindrome("") is True
    print("All palindrome tests passed.")
