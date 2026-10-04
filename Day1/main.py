from utils import is_palindrome, word_frequency, even_squares, multiplication_table


def main() -> None:
    print(is_palindrome("racecar"))             # True
    print(is_palindrome("hello"))               # False
    print(word_frequency("the cat and the hat"))  # {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}
    print(even_squares())                       # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
    multiplication_table(7)


if __name__ == "__main__":
    main()