import sys
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    bookstring = get_book_text(filepath)
    char_dict = character_count(bookstring)
    sorted_char_list = sort_by_count(char_dict)

    #Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(bookstring)} total words")
    print("--------- Character Count -------")
    for i in sorted_char_list:
        if i["letter"].isalpha():
            print(f"{i["letter"]}: {i["number"]}")
    print("============= END ===============")

main()