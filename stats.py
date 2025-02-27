def get_num_words(book_text):
    word_count = len(book_text.split())
    return word_count

def get_num_character(book_text):
    character_count = {}
    for words in book_text.lower():
        for character in words:
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    return character_count