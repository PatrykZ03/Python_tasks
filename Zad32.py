# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p7gFmEwSEc1LmsulWB8wakAX-lEYk0jb
"""

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]

print(color)