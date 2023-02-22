#!/usr/bin/env python3

def return_evens(num_list):
    evens = [num for num in num_list if (num/2).is_integer()]
    return evens

def make_exclamation(sentence_list):
    bangs = [each + "!" for each in sentence_list]
    return bangs