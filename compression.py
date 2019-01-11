# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 01:54:44 2018

@author: Swetha Srikanthan
"""

def compression(S):
    op = []
    for item in S:
        comp = ""
        count = 1
        for i in range(1, len(item)): 
            if item[i] == item[i-1]:
                count = count + 1
            else:                
                comp = comp + item[i-1] + str(count)      
                count = 1
        comp = comp + item[-1] + str(count)  
        print(comp)
        op.append(comp)
    return op
            
    
    

def main():
    inp = ["aaabbdddefgg","sweth","arram", "aadhhvvanaa"]
    op = (compression(inp))
    print(op)
    
if __name__ == "__main__":
    main()