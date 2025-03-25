from stats import count_words, character_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    bookstring = get_book_text("books/frankenstein.txt")
    print(f"{count_words(bookstring)} words found in the document")
    char_dict = character_count(bookstring)
    for i in char_dict:
        print(f"'{i}': {char_dict[i]}")

main()