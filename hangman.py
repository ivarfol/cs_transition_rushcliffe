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

def overlap_outp(ovrl, not_in, count):
    hangman = ['\n\n\n\n\n\u2514\u2500\u2500\u2500\u2500\u2500',
               '\u250C\n\u2502\n\u2502\n\u2502\n\u2502\n\u2514\u2500\u2500\u2500\u2500\u2500',
               '\u250C\u2500\u2500\u2500\u2510\n\u2502\n\u2502\n\u2502\n\u2502\n\u2514\u2500\u2500\u2500\u2500\u2500',
               '\u250C\u2500\u2500\u2500\u2510\n\u2502\n\u2502\n\u2502\n\u2502\n\u2514\u2500\u2500\u2500\u2500\u2500',
               '\u250C\u2500\u2500\u2500\u2510\n\u2502   \u25CB\n\u2502\n\u2502\n\u2502\n\u2514\u2500\u2500\u2500\u2500\u2500',
               '\u250C\u2500\u2500\u2500\u2510\n\u2502   \u25CB\n\u2502   \u2502\n\u2502\n\u2502\n\u2514\u2500\u2500\u2500\u2500\u2500',
               '\u250C\u2500\u2500\u2500\u2510\n\u2502   \u25CB\n\u2502  \u2571\u2502\n\u2502\n\u2502\n\u2514\u2500\u2500\u2500\u2500\u2500',
               '\u250C\u2500\u2500\u2500\u2510\n\u2502   \u25CB\n\u2502  \u2571\u2502\u2572\n\u2502\n\u2502\n\u2514\u2500\u2500\u2500\u2500\u2500',
               '\u250C\u2500\u2500\u2500\u2510\n\u2502   \u25CB\n\u2502  \u2571\u2502\u2572\n\u2502  \u2571\n\u2502\n\u2514\u2500\u2500\u2500\u2500\u2500',
               '\u250C\u2500\u2500\u2500\u2510\n\u2502   \u25CB\n\u2502  \u2571\u2502\u2572\n\u2502  \u2571 \u2572\n\u2502\n\u2514\u2500\u2500\u2500\u2500\u2500']
    for i in range(len(ovrl)):
        print(ovrl[i], end='')
    print()
    if len(not_in):
        print(f'\nLetters that are not in the word:\n{not_in}')
    if count != 0:
        print(hangman[count - 1])

def overlap_comparison(overl, wor):
    same = True
    for j in range(len(overl)):
        if overl[j] != wor[j]:
            same = False
            break
    return(same)

for _ in range(len(word)):
    overlap.append('_')

while count < 10:
    overlap_outp(overlap, not_in_word, count)
    print(f'You have {10 - count} tryes left')
    guess = input('Your guess:\n')
    while len(guess) != len(word) and (len(guess) != 1 or guess in not_in_word):
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

overlap_outp(overlap, not_in_word, count)
print(f'Correct answer:\n{word}')
if flag:
    print('You won')
else:
    print('You are out of guesses')