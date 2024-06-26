# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p7gFmEwSEc1LmsulWB8wakAX-lEYk0jb
"""

# Define a function named find_longest_word that takes a list of words as the argument, 'words_list'.
def find_longest_word(words_list):
    word_len = []

    for n in words_list:
        word_len.append((len(n), n))

    word_len.sort()

    return word_len[-1][0], word_len[-1][1]

result = find_longest_word(["WSB", "Merito", "Warszawa"])

print("\nLongest word: ", result[1])
print("Length of the longest word: ", result[0])