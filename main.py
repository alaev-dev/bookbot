from stats import get_num_words, get_letter_freq, sort_dict
import sys


def get_book_text(path):
    print(f"Analyzing book found at {path}...")
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")

    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    unsorted_freq = get_letter_freq(book)
    freq = sort_dict(unsorted_freq)

    print("--------- Character Count -------")

    for item in freq:
        char = item["char"]
        num = item["num"]

        if not char.isalpha():
            continue

        print(f"{char}: {num}")

    print("============= END ===============")


main()
