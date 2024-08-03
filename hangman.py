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
print(word)

def overlap_outp(ovrl):
    for i in range(len(ovrl)):
        print(ovrl[i], end='')
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
    overlap_outp(overlap)
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
    else:
        if guess == word:
            flag = True
            break
        else:
            count += 1

print(f'Correct answer: {word}')
if flag:
    print('You won')
else:
    print('You are out of guesses')