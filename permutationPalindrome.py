# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 01:49:37 2018

@author: Swetha Srikanthan
"""


#input- array of strings
#output- boolean array for each string
def palindromePermutation(arr):
    op = []
    
    for item in arr:
        dictt = {}
        length = 0
        flag = 0
        
        for ch in item:
            dictt[ch] = 0
            length += 1
        for ch in item:
            dictt[ch] += 1
        
        if length % 2 == 0:
            print(item)
            print(op)
            for item in dictt.values():
                if item %2 != 0 :
                    op.append("false")
                    flag = 1
                    break
            if(not flag):
                op.append("True")
            
        else:
            print(item)
            print(op)
            odd_count = 0
            for item in dictt.values():
                if item %2 !=0 and odd_count == 0:
                    odd_count +=1
                elif item %2 !=0 and odd_count != 0:
                    op.append("false")
                    flag = 1
                    break
            if(not flag):
                op.append("True")
            
    return op

    

def main():
    inp = ["malamala","sweth","arrra", "aadhavan"]
    op = (palindromePermutation(inp))
    print(op)
    
if __name__ == "__main__":
    main()