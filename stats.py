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

def sort_on(dict):
    return dict["number"]

def sort_by_count(char_dict):
    sort_list = []
    for i in char_dict:
        temp_dict = {"letter": i, "number": char_dict[i]}
        sort_list.append(temp_dict)
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
    

