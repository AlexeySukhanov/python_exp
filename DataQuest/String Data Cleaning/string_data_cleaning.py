#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
String data cleaning
Created on Tue Jun 16 01:55:55 2020

@author: user
"""

cleaning_dict = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z', ' ': '_', ',': '.'}
text_to_clean = "The roOm temPeraTUre is 12,5 deGrEes ceLSIus buT oUtsiDE iT IS 20.6 degreeS"

cleaned_text = ''
for letter in text_to_clean:
    if letter in cleaning_dict:
        cleaned_text += cleaning_dict[letter]
    else:
        cleaned_text += letter
print(cleaned_text)