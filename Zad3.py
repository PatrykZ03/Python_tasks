# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p7gFmEwSEc1LmsulWB8wakAX-lEYk0jb
"""

def string_both_ends(str):
    if len(str) < 2:
        return ''

    return str[0:2] + str[-2:]

print(string_both_ends('Patryk'))
print(string_both_ends('Pa'))
print(string_both_ends('P'))