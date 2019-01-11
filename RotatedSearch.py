# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:15:03 2018

@author: Swetha Srikanthan
"""

class Solution(object):
    def RotatedSearch(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,n-4):
            for j in range(i+1,n-3):
                for k in range(j+1,n-2):
                    for l in range(k+1,n-1):
                        if arr[i]+arr[j]+arr[k]+arr[l] == elem:
                            return i,j,k,l 


        return 
     
        
        
if __name__ == "__main__": 
    Input = [-1,-2,3,-4,5,7,8]
    Obj = Solution()
    print(Obj.Sumelem(Input))
    
    #7 3 8 2 9 3 8 4 7 
    #i           j k l         



                  