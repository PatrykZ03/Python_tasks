# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p7gFmEwSEc1LmsulWB8wakAX-lEYk0jb
"""

def last(n):
    return n[-1]

def sort_list_last(tuples):
    return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))