# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:48:15 2018

@author: Swetha Srikanthan
"""

#Find the elem = sum of every other elem in list

class Solution(object):
    def Sumelem(self, nums,gsum):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(gsum)
        
        for i in range(0,n):
            for j in range(0,n):
                if (i == j == gsum):
                    return i
                
                
        


        return 
     
        
        
if __name__ == "__main__": 
    Input = [-1,-2,3,-4,5,7,8]
    Obj = Solution()
    print(Obj.Sumelem(Input,8))