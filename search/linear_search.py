#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:08:26 2024

@author: iaroslav
"""
state_arr = ['Georgia', 'Delaware', 'Alabama', 'California']
state_to_find = input('What state do you want to find?\n').capitalize()
for i in range(len(state_arr)):
    if state_to_find == state_arr[i]:
        print(f'Item found at position {state_arr.index(state_to_find)}')
    elif i == len(state_arr) - 1:
        print('Item not found')