# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p7gFmEwSEc1LmsulWB8wakAX-lEYk0jb
"""

def printValues():
    l = list()
    for i in range(1, 31):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])

printValues()