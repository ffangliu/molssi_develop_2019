"""
string_util.py
A short description of the project.

Misc. string processing functions
"""
import numpy as np

def title_case(sentence):

    """
    Convert a string to title case.

    Title case means that the first character of every word is capitialzed and every
    other word is lower case

    Parameters
    -------------
    setentence : string
        String to be converted to title case

    Returns
    -------------
    converted_sentence : string
        String that conforms to the definition of title case

    """

    # check input is a string
    if not isinstance(sentence, str):
        raise TypeError('Input [%s] must be a string' %(str(sentence)))

    if len(sentence) == 0:
        raise IndexError('String cannot be empty')

    # remove training whitespace (avoids some weird edge-cases) then split by
    # whitespace
    sentence = sentence.strip()
    split_string = sentence.split(' ' )
    print(split_string)
    
    # initialzie an empty list, cycle through each 'word', splitting the word into
    # first letter and all other letters, reconstructing according to the TitleCase
    # rules
    new_words=[]
    for word in split_string:   
        if len(word) == 0:
            continue
        new_words.append(word[0].upper() + word[1:].lower())

    if len(new_words) == 0:
        raise TypeError('Cannot pass a string with all whitespce!')

    return " ".join(new_words)
