"""
File: anagram.py
Name: Annby
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    while True:
        s = input("Find anagrams for: ")
        if s == EXIT:
            break
        start = time.time()
        find_anagrams(s)
        ####################
        #                  #
        #       TODO:      #
        #                  #
        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    dictionary = []
    with open(FILE, 'r') as f:
        dictionary = [line.strip() for line in f]
    return dictionary


def find_anagrams(s):
    """
    Find and print all anagrams of the string s.
    :param s: the words entered by the user
    :return: list of found word puzzles
    """
    dictionary = read_dictionary()
    anagrams = []
    find_anagrams_helper(s, "", [], anagrams, dictionary)
    print(f"{len(anagrams)} anagrams: {anagrams}")
    return anagrams


def find_anagrams_helper(s, current, used_indices, anagrams, dictionary):
    """
    Recursively search and generate all possible anagrams.
    :param s: the words entered by the user
    :param current: the currently generated word puzzle
    :param used_indices: used alphabetical indices
    :param anagrams: used to store found anagrams
    :param dictionary: English word dictionary
    """
    if len(current) == len(s):
        if current in dictionary and current not in anagrams:
            print("searching...")
            anagrams.append(current)
            print(f"Found: {current}")
    else:
        for i in range(len(s)):
            if i not in used_indices:
                used_indices.append(i)
                if has_prefix(current + s[i]):
                    find_anagrams_helper(s, current + s[i], used_indices, anagrams, dictionary)
                used_indices.pop()


def has_prefix(sub_s):
    """
    Check if sub_s is a prefix of a word in the dictionary.
    :param sub_s: currently generated word puzzle prefix
    :return: Returns True if there is a matching prefix, False otherwise
    """
    dictionary = read_dictionary()
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
