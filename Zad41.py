# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p7gFmEwSEc1LmsulWB8wakAX-lEYk0jb
"""

import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print('Original dictionary : ',d)

sorted_d = sorted(d.items(), key=operator.itemgetter(1))

print('Dictionary in ascending order by value : ',sorted_d)

sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1), reverse=True))

print('Dictionary in descending order by value : ',sorted_d)