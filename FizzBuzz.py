# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:50:11 2018

@author: Swetha Srikanthan
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a = []
        for i in range(1,n+1):
            if (i%15 == 0):
                a.append("FizzBuzz")
            elif (i%3 == 0):
                a.append("Fizz")
            elif (i%5 == 0):
                a.append("Buzz")
            else:
                a.append(str(i))
        return a 
    
    def fizzBuzz2(self,n):
        return [("Fizz" if i%3 ==0 else '')+("Buzz" if i%5 ==0 else'') if i%5==0 or i%3==0 else str(i) for i in range(1,n+1)]
          
        
if __name__ == "__main__": 
    #Input = [1,2,3,4,5,6,7,8,9,10,12,13,15,30]
    Obj = Solution()
    print(Obj.fizzBuzz2(30))