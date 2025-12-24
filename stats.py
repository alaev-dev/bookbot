def get_num_words(book):
    return len(book.split())


def get_letter_freq(book):
    store = {}

    for word in book.split():
        for letter in word:
            small_letter = letter.lower()

            if small_letter not in store:
                store[small_letter] = 1
            else:
                store[small_letter] += 1

    return store


def sort_dict(dict):
    arr = []

    for key in dict:
        arr.append({"char": key, "num": dict[key]})

    arr.sort(reverse=True, key=lambda value: value["num"])

    return arr
