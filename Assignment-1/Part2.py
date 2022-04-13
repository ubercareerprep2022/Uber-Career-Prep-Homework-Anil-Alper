#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 20:05:31 2022

@author: Anıl Alper
"""

def isStringPermutation(s1: str, s2: str) -> bool:
    s1_dict = dict()
    s2_dict = dict()
    
    if len(s1) != len(s2):
        return False
    
    for char in s1:
        if s1_dict.get(char) != None:
            s1_dict[char] += 1
        else:
            s1_dict[char] = 1
    
    for char in s2:
        if s1_dict.get(char) == None:
            return False
        
        if s2_dict.get(char) == None:
            s2_dict[char] = 1
        else:
            s2_dict[char] += 1
         
        if s2_dict[char] > s1_dict[char]:
            return False
    
    return True

print(isStringPermutation("asdf", "fsad"))
print(isStringPermutation("asdf", "fsa"))
print(isStringPermutation("fffff", "fesax"))

def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    pairs = list()
    pairs_dict = dict()
    pdict = dict()
    for n in inputArray:
        if pdict.get(n) != None:
            if pairs_dict.get((pdict[n],n)) == None:
                pairs_dict[(pdict[n], n)] = "pair"
                pairs.append((pdict[n], n))
        else:
            pdict[targetSum-n] = n
    return pairs

print(pairsThatEqualSum([1,2,4,3,3,4,4,4,4,4,5], 8))

