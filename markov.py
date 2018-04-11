"""Generate Markov text from text files."""
import sys 
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as file_:
        text_words = file_.read()

    return text_words


open_and_read_file("green-eggs.txt")    


def make_chains(text_string, number_of_words):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    # instantiating empty dict
    chains = {}
    
    # separate words by spaces
    words = text_string.split()
    # iterate over words
  
    for i in range(len(words) - number_of_words):
        # bind words into groups
        word_group = (words[i:number_of_words+i])
        # turn groups into tuples
        chain_key = tuple(word_group)
        # looks at chain_key, if returns list concatenate with existing list or dump into new list (nth word to value)
        chains[chain_key] = chains.get(chain_key, []) + [words[number_of_words + i]]
    

    return chains   
    
# import random

def make_text(chains, number_of_words):
    """Return text from chains."""

    words = []

    # generating random word from keys
    random_key = choice(chains.keys()) 
    # adding randomly selected tuple from keys and adding to words list
    words.extend(random_key[0:number_of_words])

    # loop to look 
    print chains.items()
    while True:
        # bind last nth elements of words list to tuple
        last_n_words = tuple(words[-number_of_words:])
        # check if tuple exists in chains (return list of none if not)
        value_of_tup = chains.get(last_n_words, [None])
        # generate random word from tuple list
        random_list_word = choice(value_of_tup)
        # break loop if list is none
        if random_list_word == None:
            break

        words.append(random_list_word)
    print words     
    return " ".join(words)

input_path = sys.argv[1]
number_of_words = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, number_of_words)

# Produce random text
random_text = make_text(chains, number_of_words)

print random_text
