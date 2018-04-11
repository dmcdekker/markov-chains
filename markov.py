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


def make_chains(text_string):
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
    
    chains = {}
    
    words = text_string.split()
    for i in range(len(words) - 2):
        word_pairs = (words[i], words[i + 1])
        chain_key = tuple(word_pairs)
        #looks into chains at chain_key, and adds 3rd word to value
        chains[chain_key] = chains.get(chain_key, []) + [words[i + 2]]
   
    return chains   
    
import random

def make_text(chains):
    """Return text from chains."""

    words = []

    random_key = random.choice(chains.keys()) 
    words.append(random_key[0])
    words.append(random_key[1])

    while True:
        last_two = tuple(words[-2:])
        value_of_tup = chains.get(last_two, [None]) 
        random_list_word = random.choice(value_of_tup)
        #print value_of_tup
        if random_list_word == None:
            break

        words.append(random_list_word)

    return " ".join(words)

input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
