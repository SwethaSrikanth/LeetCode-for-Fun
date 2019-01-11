# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:53:23 2018

@author: Swetha Srikanthan
"""

#136.Single Number 

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        for i in nums: 
            if nums.count(i) == 1:
                return i
        '''
        return 2 * sum(set(nums)) - sum(nums)
    

            
if __name__ == "__main__": 
    Input = [1,2,3,4,5,5,4,3,1]
    Obj = Solution()
    print(Obj.isValid(Input))