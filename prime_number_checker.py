#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 21:17:44 2024

@author: iaroslav
"""
from math import sqrt, ceil

def prinme_num_check(num):
    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0:
            return(False)
    return(True)

def num_validator(message):
    boundary = input(f'{message}\n')
    while not(boundary.isdigit() and int(boundary) > 1):
        boundary = input(f'Invalid input\nTry again\n{message}\n')
    return(int(boundary))

def binary_choice(message):
    choice = input(f'{message}\ny/n\n')
    while choice not in {'y', 'n'}:
        choice = input(f'Invalid input\nTry again\n{message}\ny/n\n')
    if choice == 'y':
        return(True)
    else:
        return(False)

prime_list = []
if binary_choice('Do you want to check numbers in an interval?'):
    lower_boundary, upper_boundary = num_validator('Input lower boundary:'), num_validator('Input upper boundary:')
    while lower_boundary >= upper_boundary:
        print('Lower boundary has to be lower than upper boundary')
        lower_boundary, upper_boundary = num_validator('Input lower boundary:'), num_validator('Input upper boundary:')
    for i in range(lower_boundary, upper_boundary + 1):
        if prinme_num_check(i):
            prime_list.append(i)
    print(*prime_list)
else:
    print(prinme_num_check(num_validator('Input a number to check:')))