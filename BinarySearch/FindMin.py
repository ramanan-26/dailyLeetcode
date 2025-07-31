from typing import List

class Solution:
    def findMin(self, arr: List[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array without duplicates.

        Parameters:
        arr (List[int]): A rotated sorted array with no duplicate values.

        Returns:
        int: The minimum element in the array.

        Time Complexity: O(log n) - Binary search is used to efficiently find the minimum.
        Space Complexity: O(1) - Only constant extra space is used.
        """
        l, r = 0, len(arr) - 1

        while l < r:
            m = (l + r) // 2

            # If middle element is less than the rightmost, the min is in the left half (including mid)
            if arr[m] < arr[r]:
                r = m
            else:
                # Min must be in the right half (excluding mid)
                l = m + 1

        # At the end of loop, l == r, pointing to the smallest element
        return arr[l]
