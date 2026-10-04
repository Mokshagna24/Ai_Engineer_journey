
def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards.
    isalnum() returns True if all characters in the string are alphanumeric
     and there is at least one character, False otherwise."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def word_frequency(sentence: str) -> dict[str, int]:
    """Count how many times each word appears."""
    counts: dict[str, int] = {}
    for word in sentence.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def even_squares(limit: int = 20) -> list[int]:
    """Squares of the even numbers from 1 to limit."""
    return [n * n for n in range(1, limit + 1) if n % 2 == 0]


def multiplication_table(n: int) -> None:
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


if __name__ == "__main__":
    # Runs ONLY when you execute: python utils.py
    print("Testing utils.py directly...")
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True


