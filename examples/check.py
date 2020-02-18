# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:27:31 2016
Function used to determine if a module contains a given function. Takes 2 arguments (module, function). Returns number of times func exist in the package (yes, only once usually, if you're not overloading). 
MUST import module first
@author: Tom
"""
def qcontain(mod, func):
    a = dir(mod)
    r = range(len(a))
    counter = 0
    for i in r:
        if a[i]==func:
            counter += 1
    print(a)        
    return counter

