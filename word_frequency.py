import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
# open file and create new string or list with contents
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
    text = text.replace("\n", " ")
    return text
# print(normalize_text("Too  Much loittle !!@@ kddk")) #checking here, it works!

def print_word_freq(filename):
    """read filename and print our words in file"""
    with open(filename) as file:
        text = file.read()

    text = normalize_text(text)
    words = []
    for word in text.split(" "):
        if word != '' and word not in STOP_WORDS:
            words.append(word)
    
    print(words)

print(print_word_freq("seneca_falls.txt"))

# print(seneca_list_lines) #testing to see if worked and it's ok!
# GET DICT OF WORD FREQUENCIES AND PRINT THEM OUt

# go through file with for loop and count how many times word is used

# print words and their frequency

# def print_word_freq(file):
#     """Read in `file` and print out the frequency of words in that file."""
#     pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
