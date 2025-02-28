import sys 
from stats import get_num_words
from stats import get_num_character
from stats import sort_on



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(path_to_file)
    word_count = get_num_words(book_text)
    character_count = get_num_character(book_text)
    sort_char = sort_on(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for key, value in sort_char.items():
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")

path_to_file = sys.argv[1]

if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    get_book_text(path_to_file)



main()