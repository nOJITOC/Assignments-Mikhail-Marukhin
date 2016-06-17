def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
def main():
	sentence1= "La la la! I'm the Lord of the ring!!!"
	words = break_words(raw_input("Input words:"))
	print_first_word(words)
	print_last_word(words)
	words
	word = sort_sentence(raw_input("Input words:"))
	print word
	print_first_and_last(sentence1)
	print_first_and_last_sorted(sentence1)
if __name__ == '__main__':
    main()
