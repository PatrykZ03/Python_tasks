# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p7gFmEwSEc1LmsulWB8wakAX-lEYk0jb
"""

def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot

print(multiply_list([1, 2, -8]))