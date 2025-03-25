def count_words(bookstring):
    word_list = []
    word_list = bookstring.split()
    return len(word_list)

def character_count(bookstring):
    char_dict = {}

    for char in bookstring.lower():
        char_dict.setdefault(char, 0)
        char_dict[char] += 1
    
    return char_dict
    

