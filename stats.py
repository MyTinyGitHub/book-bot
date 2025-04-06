
def get_book(file):
    with open(file) as book:
        return book.read()


def get_num_words(book):
    return len(book.split())

def get_letter_count(book):
    result = {}
    for letter in book:
        if not letter.isalpha():
            continue
        if letter.lower() not in result:
            result[letter.lower()] = 0
        result[letter.lower()] += 1
    return result

