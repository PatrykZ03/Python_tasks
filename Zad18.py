# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p7gFmEwSEc1LmsulWB8wakAX-lEYk0jb
"""

def first_three(str):
    if len(str) > 3:
        return str[:3]
    else:
        return str

print(first_three('ipy'))      # Output: 'ipy'
print(first_three('python'))   # Output: 'pyt'
print(first_three('py'))       # Output: 'py'