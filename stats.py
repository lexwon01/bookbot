def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    lower_words = text.lower()
    
    num_char = {}

    for char in lower_words:
        if char in num_char:
            num_char[char] += 1
        else:
            num_char[char] = 1
    return num_char

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    
    for ch in num_chars_dict:
        tmp_dict = {"char": ch, "num": num_chars_dict[ch]}
        
        sorted_list.append(tmp_dict)
    
    sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list

