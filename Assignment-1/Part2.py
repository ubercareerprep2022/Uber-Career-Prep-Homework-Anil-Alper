#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 20:05:31 2022

@author: Anıl Alper
"""

def isStringPermutation(s1: str, s2: str) -> bool:
    t1 = dict()
    t2 = dict()
    
    if len(s1) != len(s2):
        return False
    
    for c in s1:
        if c in t1:
            t1[c] += 1
        else:
            t1[c] = 1
    
    for c in s2:
        if c not in t1:
            return False
        
        if c not in t2:
            t2[c] = 1
        else:
            t2[c] += 1
         
        if t2[c] > t1[c]:
            return False
    
    return True
        
#print(isStringPermutation("asdf", "fsad"))
#print(isStringPermutation("asdf", "fsa"))
#print(isStringPermutation("fffff", "fesax"))

def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    pairs = list()
    pdict = dict()
    for n in inputArray:
        if n in pdict:
            pairs.append((pdict[n], n))
            del pdict[n]
        else:
            pdict[targetSum-n] = n
    return pairs

print(pairsThatEqualSum([1,2,3,3,4,4,5], 8))