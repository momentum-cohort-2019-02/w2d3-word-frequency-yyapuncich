import string
import collections
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
# this function is used to clean up text. I use it within the function underneath called COMPILE_LIST()
def normalize_text(text):
    """Takes text and removes punctuation and replaces whitespace with normal spaces- compressing single spaces"""
    text = text.lower()
    valid_chars = string.ascii_letters + string.whitespace + string.digits # check for valid chars add them to new var

    #remove punctuation
    new_text = ""
    for char in text:
        if char in valid_chars:
            new_text += char
    text = new_text
    cleaned_text = text.replace("\n", " ")
    return cleaned_text
# print(normalize_text("Too  Much loittle !!@@ kddk")) #checking here, it works!

def compile_list(filename):
    """read filename and print out words in file"""
    with open(filename) as file:
        text = file.read()
# the above creates a string with contents of file
    text = normalize_text(text) 
    words = []
    for word in text.split(" "):
        if word != '' and word not in STOP_WORDS:
            words.append(word)
# the above creates a list of all the words, without the stop_words
    return words

# assigning variable WORDS that uses above function to complie list of words in seneca_falls.txt
words = compile_list("seneca_falls.txt")
# print(compile_list("seneca_falls.txt"))
# count words and make new list ???? how do i ensure count matches up with specific word?
def word_count_list(list_words):
    """Goes through words and creates dictionary containing word and count"""
    number_of_word = {}
    # below for loop checks each word in list and will add it to number_of_word dictionary, if already in dictionary will tally additional number and add to value of word
    for each_word in list_words:
        if each_word not in number_of_word:
            number_of_word[each_word] = 1
        else:
            number_of_word[each_word] += 1
    return number_of_word

# assigning new variable below that uses function to make dictionary of WORD:COUNT as KEY:VALUE, then printing it out the check
word_count_dict = word_count_list(words)
print(word_count_dict)




# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)
