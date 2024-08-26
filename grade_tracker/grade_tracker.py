#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:42:19 2024

@author: iaroslav
"""
import pickle
import os
from grade_tracker_config_reader import get_settings

def main():
    config = get_settings()
    def_path = config.path_load
    save_path = config.path_save
    save_flag = True
    f_load = True
    if config.new_ask == 'yes':
        f_load = binary_choice('Do you want to load a file?')
        if f_load:
            student_dict = load(def_path)
        else:
            student_dict = {}
    else:
        if def_path == '':
            student_dict = load(def_path)
    while True:
        command = command_valid('Input a command\nadd student/add score/revert score/remove student/rename student\n/scores/save/exit\n')
        if command[:4] == 'exit':
            if not save_flag and binary_choice('Do you want to save the changes?'):
                save(save_path, student_dict, f_load)
            break
        elif command[:11] == 'add student':
            save_flag = False
            student_dict.update({command[12:]: []})
        elif command[:9] == 'add score':
            save_flag = False
            student_dict = add_score(student_dict, command[10:])
        elif command[:12] == 'revert score':
            save_flag = False
            student_dict = revert_score(student_dict, command[13:])
        elif command[:14] == 'remove student':
            save_flag = False
            student_dict = remove_student(student_dict, command[15:])
        elif command[:14] == 'rename student':
            save_flag = False
            student_dict[input('Input the new name:\n')] = student_dict[command[15:]]
            del student_dict[command[15:]]
        elif command[:4] == 'save':
            save_flag = True
            save(save_path, student_dict, f_load)
        elif command[:6] == 'scores':
            if binary_choice('Do you want to sort the dictionary?'):
                scores_print(scores_sort(get_avrg(student_dict)))
            else:
                scores_print(get_avrg(student_dict))
    return()

def load(def_path):
    if os.path.exists(def_path):
        with open(def_path,'rb') as file:
            st_dict = pickle.load(file)
        return(st_dict)
    dict_path = input('Input path to the file to load\n')
    while not os.path.exists(dict_path):
        dict_path = input('Path does not exist\nInput path to the file to load\n')
    with open(dict_path,'rb') as file:
        st_dict = pickle.load(file)
    return(st_dict)
    
def save(def_path, st_dict, f_load):
    if os.path.exists(def_path) and f_load:
        with open(def_path,'wb') as file:
            pickle.dump(st_dict, file)
        return()
    dict_path = input('Input path to the file to save the results to\n')
    while not os.path.exists(dict_path):
        print('Path does not exist')
        if binary_choice('Do you want to create a new file with this name:'):
            break
        dict_path = input('Input path to the file to save the results to\n')
    with open(dict_path,'wb') as file:
        pickle.dump(st_dict, file)
    return()

def command_valid(message):
    command = input(message)
    while (command[:11] != 'add student' or len(command) < 12) and (command[:9] != 'add score' or command.count(' ') < 3) and (command[:12] != 'revert score' or len(command) < 13) and (command[:14] != 'remove student' or len(command) < 15) and (command[:14] != 'rename student' or len(command) < 15) and command[:6] != 'scores' and command[:4] != 'save' and command[:4] != 'exit':
        command = input(message)
    return(command)

def add_score(st_dict, inp):
    inp_temp = inp.split()
    if len(inp_temp) < 2:
        return(st_dict)
    if inp[: - len(inp_temp[-1]) - 1] not in st_dict.keys():
        if binary_choice('Are you shure you want to add a student?'):
            st_dict.update({inp[: - len(inp_temp[-1]) - 1]: []})
        else:
            return(st_dict)
    score = inp_num('Input score:\n', inp_temp[-1])
    st_dict[inp[: - len(inp_temp[-1]) - 1]] = st_dict[inp[: - len(inp_temp[-1]) - 1]] + [score]
    return(st_dict)

def revert_score(st_dict, inp):
    if not inp in st_dict.keys():
        return(st_dict)
    if len(st_dict[inp]) >= 1:
        st_dict[inp] = st_dict[inp][:-1]
    return(st_dict)

def remove_student(st_dict, inp):
    if inp in st_dict.keys():
        st_dict.pop(inp)
    return(st_dict)

def inp_num(message, inp):
    while True:
        try:
            score = float(inp)
            break
        except:
            print('Has to be float or integer')
            score = float(input(message))
        inp = input()
    return(score)

def get_avrg(st_dict):
    temp = st_dict.items()
    temp_dict = {}
    temp_pair = []
    avrg_temp = 0
    for pair in temp:
        avrg_temp = 0
        temp_pair = [pair[0]]
        for score in pair[1]:
            avrg_temp += score
        if len(pair[1]) != 0:
            temp_pair += [avrg_temp / len(pair[1])]
        else:
            temp_pair += [0]
        temp_dict[temp_pair[0]] = temp_pair[1]
    return(temp_dict)

def scores_sort(temp_dict):
    return(dict(sorted(temp_dict.items(), key=lambda item: item[1], reverse=True)))

def scores_print(temp_dict):
    temp = temp_dict.items()
    for pair in temp:
        print(pair[0], end=': ')
        print(pair[1])
    return()

def binary_choice(message):
    choice = input(f'{message}\ny/n\n')
    while choice not in {'y', 'n'}:
        choice = input(f'{message}\ny/n\n')
    if choice == 'y':
        return(True)
    else:
        return(False)

if __name__ == '__main__':
    main()