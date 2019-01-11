# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 09:17:15 2018

@author: Swetha Srikanthan
"""
import sys
import math


#Find thesum of 2 elem = or closer to zero.

class Solution(object):
    def LeastSumofTwo(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        l =  0
        r = len(nums) - 1
        min_l = l
        min_r = r
        cur_sum = min_sum = math.inf
        
        if ( len(nums) < 2):
            return -1
        
        while(l<r):
            cur_sum = nums[l] + nums[r]
            
            if (abs(cur_sum) < abs(min_sum) ):
                min_sum = cur_sum
                min_l = l
                min_r = r
                
            if( cur_sum < 0 ):
                l = l+1
            else:
                r = r-1 
                
        return min_l,min_r,min_sum

        
        
if __name__ == "__main__": 
    Input = [-1,-2,0,3,-4,5,7]
    Obj = Solution()
    print(Obj.LeastSumofTwo(Input))