from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = 0
        result = []

        # Find the maximum number of candies
        for num in candies:
            if maxi < num:
                maxi = num
        
        # Check each kid
        for candy in candies:
            total = candy + extraCandies
            if maxi <= total:
                result.append(True)
            else:
                result.append(False)
        
        return result