#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 11:32:31 2024

@author: iaroslav
"""
from random import randint
word_list = ['word', 'animal', 'country']
word = word_list[randint(0, len(word_list) - 1)]
overlap = []
flag = False
count = 0
not_in_word = ''

def overlap_outp(ovrl, not_in):
    for i in range(len(ovrl)):
        print(ovrl[i], end='')
    if len(not_in):
        print(f'\nLetters in the word:\n{not_in}')
    else:
        print()

def overlap_comparison(overl, wor):
    same = True
    for j in range(len(overl)):
        if overl[j] != wor[j]:
            same = False
            break
    return(same)

for _ in range(len(word)):
    overlap.append('_')

while count < 11:
    overlap_outp(overlap, not_in_word)
    print(f'You have {11 - count} tryes left')
    guess = input('Your guess:\n')
    while len(guess) != len(word) and len(guess) != 1:
        guess = input('Try again\nYour guess:\n')
    if len(guess) == 1:
        if guess in word:
            for letter_index in range(len(word)):
                    if word[int(letter_index)] == guess:
                        overlap[letter_index] = guess
            if overlap_comparison(overlap, word):
                flag = True
                break
        else:
            count += 1
            not_in_word += guess
    else:
        if guess == word:
            flag = True
            break
        else:
            count += 1

print(f'Correct answer:\n{word}')
if flag:
    print('You won')
else:
    print('You are out of guesses')