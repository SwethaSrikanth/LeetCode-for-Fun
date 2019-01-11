# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 00:06:42 2018

@author: Swetha Srikanthan
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        cur_sum = max_sum = nums[0]
        
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum
     
        
        
if __name__ == "__main__": 
    Input = [1,2,3,4,5,6,7,8,9,10,12,13,15,30]
    Obj = Solution()
    print(Obj.maxSubArray(Input))