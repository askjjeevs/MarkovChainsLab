"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as stri_ng; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    content = open(file_path)
    file_to_read = content.read()
    content.close
    # print (content)

    return file_to_read


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
    words = text_string.split()

    chains = {}
    
    #loop over words 
    for i in range(len(words) - 2):
    # assign the keys and values to its own tuple and list 
        key = (words[i], words[i + 1])
        value = words [i+2]
    # add key to chain; first check if key is in chain
        if key not in chains:
            chains[key] = []
        else:
            chains[key].append(value)

    # print(chains)
    return chains

def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))  # key becomes a tuple: randomly chosen from a newly created list of keys of the 'chains'{} directory 
    words = [key[0], key[1]]  # ('would', 'you')
    word = choice(chains[key])

    # Keep looping until we reach a value of None
    # (which would mean it was the end of our original text)
    # Note that for long texts (like a full book), this might mean
    # it would run for a very long time.

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])

    return ' '.join(words)

# input_path = 'green-eggs.txt'

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
