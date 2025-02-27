from stats import get_num_character

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    character_count = get_num_character(book_text)
    print(character_count)

main()