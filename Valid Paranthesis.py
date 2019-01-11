# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 22:36:32 2018

@author: Swetha Srikanthan
"""

#92: Valid Paranthesis 


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openingb = '({['
        closingb = ')}]'
        dictb = dict(zip(closingb,openingb))
        stack = []
        for char in s:
            if char in openingb:
                stack.append(char)
            else:
                try:       
                    if stack.pop() != dictb[char]:
                        raise ValueError
                except (KeyError, ValueError, IndexError):
                    return False
        return len(stack) == 0  


            
if __name__ == "__main__": 
    Input = '()[]{}'
    Obj = Solution()
    print(Obj.isValid(Input))
