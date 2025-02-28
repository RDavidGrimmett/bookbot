from stats import get_num_words
from stats import get_num_character
from stats import sort_on

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = get_num_words(book_text)
    character_count = get_num_character(book_text)
    sort_char = sort_on(character_count)
    for key, value in sort_char.items():
        print(f"{key}: {value}")

main()