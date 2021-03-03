"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    sentence = ""
    input_file = open(file_path)
    for line in input_file:
        line = line.rstrip().split(" ")
        for word in line:
            sentence += word + " "
    
    return sentence


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    text_list = text_string.split(" ")

    chains = []
    
    for i in range(len(text_list)-3):
        chains_list = [text_list[i], text_list[i+1]]
        chains.append(chains_list)
    
    
    """Create a dictionary with our tuples as the keys and initialize all 
    values as empty lists"""
    chains_tuples = {}
    
    for chain in chains:
        first, second = chain
        chains_tuples[(first, second)] = [] 
    
    for chain in chains_tuples.keys():
        for j in range(len(text_list)):
            if chain[0] == text_list[j] and chain[1] == text_list[j+1]:
                chains_tuples[chain].append(text_list[j+2])

    return chains_tuples

import random

def make_text(dictionary):
    """Return text from chains."""
    """Generate a dictionary and return the first random key as a list"""
    words = []
    first_keys = list(dictionary.keys())
    word_1 = first_keys[random.randint(0, len(first_keys))]
    word_list = list(word_1) 
    words += word_list

    """generate a random value from the second word of the first key"""
    word_2 = word_1[1] #second value of the first word pair
    random_string = ""
    for i in range(len(first_keys)):
       if word_2 == first_keys[i][0]: #if 2nd value = first value of the first word pair in the list
            words.append(first_keys[i][1]) 
    return ' '.join(words)
 
input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
