#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 21:31:11 2024

@author: iaroslav
"""
word = input('Input a word/phrase ro check if it is a polindrome:\n').lower()

for ch in ['!', '\\', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[' ']', '^', '_', '`', '{', '|', '}', '~',]:
    if ch in word:
        word = word.replace(ch, '')

if word == word[::-1]:
    print('The word/phrase is a palindrome')
else:
    print('The word/phrase is not a palindrome')