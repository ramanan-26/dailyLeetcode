class Solution:
    def maxScore(self, s: str) -> int:  
        binary = {'0':0,'1':1}
        totalSum = 0
        left,max_sum = 0,0

        #preCalculate
        for num in s:
            if num == '1': totalSum += 1
        for i in range(len(s)-1):
            if s[i] =='0':
                left += 1
            else:
                 totalSum-= 1
            max_sum = max(max_sum,left+totalSum)
        return max_sum
        

        
        