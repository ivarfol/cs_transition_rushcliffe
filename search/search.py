#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:36:59 2024

@author: iaroslav
"""
state_arr = ['Georgia', 'Delaware', 'Alabama', 'California']
state_to_find = input('What state do you want to find?\n').capitalize()
if state_to_find in state_arr:
    print(f'Item found at position {state_arr.index(state_to_find)}')
else:
    print('Item not found')