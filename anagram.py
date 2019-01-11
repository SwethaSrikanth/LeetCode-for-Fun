# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 01:56:24 2018

@author: Swetha Srikanthan
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 01:54:44 2018

@author: Swetha Srikanthan
"""

def anagramheck(A1, A2):
    dictt = {}
    dictt2 = {}
    if len(A1)!=len(A2):
        return False
    
    A = set(A1)
    if A != set(A2):
        return False 
    
    for ch in A1:
        if ch in dictt:
            dictt[ch] += 1
        else:
           dictt[ch] = 1   
           
    for ch in A2:
        dictt2[ch] = 0
    for ch in A2:
        dictt2[ch] += 1
           
    for ch in A:
        if dictt[ch] != dictt2[ch]:
            return False
        
    return True
    
    
    

def main():
    print(anagramheck("swetha","swehjhjhjhjtta"))
    print(anagramheck("swetha","thaeswww"))

if __name__ == "__main__":
    main()