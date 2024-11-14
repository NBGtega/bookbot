def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_each_characters_count(text)
    chars_sorted_list = sorted_characters(char_count)
    print(f" --- Begin report of {book_path} ---")
    print(f"There were {num_words} words found in the Frankenstein book")
    print()
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- end report ---")


def get_num_words(text): 
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def sorted_characters(characters_count):
    sorted_list = []
    for char, values in characters_count.items():
        sorted_list.append({"char": char, "num": values})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_each_characters_count(text):
    characters_count = {}
    for char in text.lower():
        if char in characters_count:
            characters_count[char] += 1
        else:
            characters_count[char] = 1
    return characters_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

    
main()


# done = False
# while not done:
#     user_input = input("Type in any word here or (quit) to end program: ")
#     if user_input == "quit":
#         done = True
#     else:
#         joined_words = user_input.split()
#         num_words = len(joined_words)
#         characters_count = {}
#         for characters in user_input:
#             lowered_char = characters.lower()
#             if lowered_char in characters_count:
#                 characters_count[lowered_char] += 1
#             else: 
#                 characters_count[lowered_char] = 1
#         # sorted_list = []
#         for char,values in characters_count.items():
#             print(f"char {char} has value {values}")
#         print(characters_count)        
#     print(f"The input has {num_words}")





