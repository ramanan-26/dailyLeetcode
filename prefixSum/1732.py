class Solution:
    def largestAltitude(self, gain):
        maxi = 0 
        total=0
        for num in gain:
            total += num
            maxi = max(total,maxi)
        return maxi
