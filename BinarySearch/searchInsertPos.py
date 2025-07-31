from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Searches for the target in a sorted list of integers and returns the index if found.
        If the target is not found, returns the index where it would be inserted to maintain order.

        Parameters:
        nums (List[int]): A list of sorted integers.
        target (int): The target value to search for or insert.

        Returns:
        int: The index of the target if found, or the insertion index if not found.

        Time Complexity: O(log n)
            - Binary search is used, which halves the search space with each step.
        Space Complexity: O(1)
            - Only a constant amount of extra space is used (for pointers and mid index).
        
        Examples:
        ---------
        >>> Solution().searchInsert([1,3,5,6], 5)
        2
        >>> Solution().searchInsert([1,3,5,6], 2)
        1
        >>> Solution().searchInsert([1,3,5,6], 7)
        4
        >>> Solution().searchInsert([1,3,5,6], 0)
        0
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            # Found the target at index m
            if nums[m] == target:
                return m
            # Target is smaller than mid element; look left
            elif nums[m] > target:
                r = m - 1
            # Target is larger than mid element; look right
            else:
                l = m + 1

        # Target not found; return the position where it should be inserted
        return l
