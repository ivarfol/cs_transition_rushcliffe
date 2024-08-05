#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:58:45 2024

@author: iaroslav
"""
from random import randint
from config_reader import get_settings

flag = False
wrong_place = []
overlap = []
str_to_guess = []
to_be_guessed = []
config = get_settings()

def binary_choice(message):
    choice = input(f'{message}\ny/n\n')
    while choice not in {'y', 'n'}:
        choice = input(f'Invalid input\nTry again\n{message}\ny/n\n')
    if choice == 'y':
        return(True)
    else:
        return(False)

if config.simultaneous == 'yes':
    num_of_wordles = input('How many numbers do you want to guess simultaneously (1 - 10)?\n')
    while not(num_of_wordles.isdigit() and int(num_of_wordles) >= 1 and int(num_of_wordles) <= 10):
        num_of_wordles = input('Invalid input\nTry again\nHow many numbers do you want to guess simultaneously (1 - 10)?\n')
    num_of_wordles = int(num_of_wordles)
else:
    num_of_wordles = config.simultaneous_num

for rnd_num in range(int(num_of_wordles)):
    str_to_guess.append(randint(0, 9999))
    str_to_guess[rnd_num] = '%04d'%str_to_guess[rnd_num]
    overlap.append('')
    wrong_place.append('')
    to_be_guessed.append(True)
    
if config.ask_wordle == 'yes':
    wordle = binary_choice('Do you want to play with wordle extension\ny/n\n')
else:
    if config.wordle == 'yes':
        wordle = True
    else:
        wordle = False
        
if config.ask_tries == 'yes':
    num_of_guesses = input('How many tries do you want to give yourself (5 - 20)?\n')
    while not(num_of_guesses.isdigit() and int(num_of_guesses) >= 5 and int(num_of_guesses) <= 20):
        num_of_guesses = input('Invalid input\nTry again\nHow many tries do you want to give yourself (5 - 20)?\n')
else:
    num_of_guesses = config.tries

for i in range(int(num_of_guesses)):
    guess = input(f'You have {int(num_of_guesses) - i} guesses left\nguess 4 digits:\n')
    while not (guess.isdigit() and len(guess) == 4):
        guess = input('Unacceptable guess\nguess 4 digits:\n')
    if num_of_wordles > 1:
        for _ in range(num_of_wordles):
            print(f'{guess} ', end='')
        print()
    for y in range(num_of_wordles):
        for j in range(4):
            if guess == str_to_guess[y] or not to_be_guessed[y]:
                to_be_guessed[y] = False
                overlap[y] = str_to_guess[y]
            elif guess[j] == str_to_guess[y][j]:
                overlap[y] += guess[j]
            else:
                overlap[y] += '*'
        for x in range(4):
            if not to_be_guessed[y]:
                wrong_place[y] = '    '
            elif wordle and guess[x] != str_to_guess[y][x] and guess[x] in str_to_guess[y] and overlap[y].count(guess[x]) < str_to_guess[y].count(guess[x]):
                wrong_place[y] += guess[x]
            else:
                wrong_place[y] += '*'
    print(*overlap)  
    flag = True
    wrong_place_flag = False
    for k in range(num_of_wordles):
        if to_be_guessed[k]:
            flag = False
            overlap[k] = ''
            if wordle:
                if wrong_place[k] != '****':
                    wrong_place_flag = True
    if wordle and wrong_place_flag:
        print('Digits in the number, but in the wrong place:')
        print(*wrong_place)
    else:
        print('No digits in incorrect places guessed')
    for l in range(num_of_wordles):
        if to_be_guessed:
            wrong_place[l] = ''
    if flag:
        break
if num_of_wordles == 1:
    print('Correct answer:')
else:
    print('Correct answers:')
print(*str_to_guess)
if flag:
    print('You won')
else:
    print('You are out of guesses')