# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p7gFmEwSEc1LmsulWB8wakAX-lEYk0jb
"""

# Define a function named remove_char that takes two arguments, 'str' and 'n'.
def remove_char(str, n):
    first_part = str[:n]

    last_part = str[n+1:]

    return first_part + last_part

print(remove_char('Patryk', 0))
print(remove_char('Patryk', 3))
print(remove_char('Patryk', 5))