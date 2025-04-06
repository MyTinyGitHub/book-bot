from stats import get_num_words, get_book, get_letter_count


def main():
    book_uri = "./books/frankenstein.txt"
    book = get_book(book_uri)
    word_count = get_num_words(book)
    letter_count = sorted(get_letter_count(book).items(), key= lambda item: -item[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_uri}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for key, value in letter_count:
        print(f"{key}: {value}")
    print("============= END ===============")

main()
