def print_upper_words(words):
    """Print words on seperate lines"""

    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """Prints words only starting with "e"""

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """Passes in a set of letters and prints only
     words that start with one of those letters"""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print (word.upper())