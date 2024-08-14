#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 19:46:09 2024

@author: iaroslav
"""
import numpy as np
import os

def path_to_file_enc():
    u_path = input('Input the path to the first file:\n')
    while not os.path.exists(u_path):
        u_path = input('Invalid path\nTry again\nInput the path to the first file:\n')
    return(u_path)

def path_to_file_overwrite():
    u_choice = False
    while not u_choice:
        u_path = input('Input the path to the file to overwrite:\n')
        if os.path.exists(u_path):
            u_choice = binary_choice('You are overwriting a file, continue?')
        else:
            u_choice = binary_choice('Are you shure you want to create a file?')
    return(u_path)

def bin_list():
    with open(path_to_file_enc(), 'rb') as file:
        arr = file.read()
    np_arr = np.array([a for a in arr], dtype=np.uint8)
    return(np_arr)

def bin_outp(outp):
    with open(path_to_file_overwrite(), 'wb') as file:
        file.write(outp)

def bin_converter(text):
    text_code = []
    for i in range(len(text)):
        text_code.append(ord(text[i]))
    return(np.array(text_code))

def key_validator():
    boundary = input('Input a key (1-255):\n')
    while not(boundary.isdigit() and int(boundary) >= 0 and int(boundary) <= 256):
        boundary = input('Invalid input\nTry again\nInput a key (1-255):\n')
    return(int(boundary))

def decriptor_outp(decripted):
    for i in range(len(decripted)):
        print(chr(decripted[i]), end='')
    print()

def binary_choice(message):
    choice = input(f'{message}\n1/0\n')
    while choice not in {'1', '0'}:
        choice = input(f'Invalid input\nTry again\n{message}\n1/0\n')
    if choice == '1':
        return(True)
    else:
        return(False)
    
def num_validator(message):
    number = input(f'{message}\n')
    while not(number.isdigit() and int(number) < 26):
        number = input(f'Invalid input\nTry again\n{message}\n')
    return(int(number))

#%%

def caesar_cipher_encr():
    encript = input('Input the text to encript:\n')
    encripted = ''
    shift = num_validator('input a shift:')
    for letter in encript:
        temp = ord(letter)
        if temp > 96 and temp < 123:
            temp_border = 122
        elif temp > 64 and temp < 91:
            temp_border = 90
        elif temp > 47 and temp < 58:
            temp_border = shift % 10
        else:
            encripted += letter
            continue
        if temp > 47 and temp < 58 and temp + temp_border > 57:
            m_shift = temp_border - 10
        elif temp > 47 and temp < 58:
            m_shift = temp_border
        elif temp + shift > temp_border:
            m_shift = shift - 26
        else:
            m_shift = shift
        encripted += chr(temp + m_shift)
    print(encripted)

def caesar_cipher_decr():
    encript = input('Input the text to decript:\n')
    encripted = ''
    shift = - num_validator('input a shift:')
    for letter in encript:
        temp = ord(letter)
        if temp > 96 and temp < 123:
            temp_border = 97
        elif temp > 64 and temp < 91:
            temp_border = 65
        elif temp > 47 and temp < 58:
            temp_border = - (- shift % 10)
        else:
            encripted += letter
            continue
        if temp > 47 and temp < 58 and temp + temp_border < 48:
            m_shift = temp_border + 10
        elif temp > 47 and temp < 58:
            m_shift = temp_border
        elif temp + shift < temp_border:
            m_shift = shift + 26
        else:
            m_shift = shift
        encripted += chr(temp + m_shift)
    print(encripted)
    
def code_cipher_encr():
    if binary_choice('Do you want to encript a file(1) or a text(0)?'):
        code = bin_list() ^ key_validator()
        bin_outp(code)
    else:
        text_m = bin_converter(input('Input the text:\n'))
        code = text_m ^ key_validator()
        print(code)

def code_cipher_decr():
    if binary_choice('Do you want to decript a file(1) or a text(0)?'):
        code = bin_list() ^ key_validator()
        bin_outp(code)
    else:
        u_decript = input('Input list to decript:\n')[1:-1].split()
        for _ in range(u_decript.count('\n')):
            u_decript.remove('\n')
        for _ in range(u_decript.count('')):
            u_decript.remove('')
        for i in range(len(u_decript)):
            u_decript[i] = int(u_decript[i])
        decriptor_outp(np.array(u_decript) ^ key_validator())

#%%

def main():
    if binary_choice('Do ypu want to encript(1) or decript(0)?'):
        if binary_choice('Do you want to use Caesars cipher(1), or simbol code cipher(0)?'):
            caesar_cipher_encr()
        else:
            code_cipher_encr()
    else:
        if binary_choice('Did you use Caesars cipher(1), or simbol code cipher(0)?'):
            caesar_cipher_decr()
        else:
            code_cipher_decr()
            
if __name__ == '__main__':
    main()