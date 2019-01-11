# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 12:19:35 2018

@author: Swetha Srikanthan
"""

# Find four elements whose sum is the Sum given 
#dicti= { x : i for i,x in enumerate(Input)}   
#code
#code
class Solution(object):
    def FourSum(self,n, nums,nsum):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        
        #create dict with two sum from (2 place to last)
        for k in range(2,n-1):
            for l in range(k+1,n):
                cur_sum = nums[k]+nums[l]
                li = []
                if (cur_sum not in d):
                    li.insert(0,[k,l])
                    d[cur_sum] = li
                else:
                    d[cur_sum].append([k,l])

        for i in range(0,n-3):
            for j in range(i+1,n-2):
                    elem = nsum - (nums[i] + nums[j])
                    if elem in d:
                        for e in d[elem]:
                            if (i not in e and j not in e):
                                #print(i,j,elem,d[elem])
                                return 1   
        return 0
    
if __name__ == "__main__": 
    Obj = Solution()
    T =  1
    while(T):
        try:
            n = 11
            #arr = "37 28 16 44 36 37 43 50 22 13 28 41 10 14 27 41 27 23 37 12 19 18 30 33 31 13 24 18 36 30 3 23 9 20 18 44 7 12 43 30 24 22 20 35 38 49 25 16 21 14 27 42 31 7 24 13 21 47 32 6 26 35 28 37 6 47 30 14 8 25 46 33 46 15 18 35 15 44 1 38 9 27 29 39"
            arr ="44 28 41 27 50 3 32 38 28 50 8"
            arr.strip()
            arr = arr.split(" ")
            #print(arr)
            arr = [int(i) for i in arr]
            elem = 67
        except EOFError:
            break
        print(Obj.FourSum(n,arr,elem))
        T = T - 1


'''/
if __name__ == "__main__": 
    Obj = Solution()
    T = int(input())
    while(T):
        try:
            n = int(input())
            arr = input().strip()
            arr = arr.split(" ")
            #print(arr)
            arr = [int(i) for i in arr]
            elem = int(input())
        except EOFError:
            break
        print(Obj.FourSum(n,arr,elem))
        T = T -1
        
 '''
        

        
