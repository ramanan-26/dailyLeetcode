

class Solution:
    """
    A class to perform binary search on each row of a 2D matrix to find a target value.

    Time Complexity:
        O(m * log n), where m is the number of rows and n is the number of columns.
        - Binary search is applied to each row individually.
    
    Space Complexity:
        O(1), constant space.
        - No extra data structures used, only a few integer pointers.
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Search for a target integer in a 2D matrix.

        Each row of the matrix is sorted in ascending order.
        There is no guarantee on the relationship between rows.

        Args:
            matrix (List[List[int]]): 2D list of integers.
            target (int): Value to search for.

        Returns:
            bool: True if target is found, False otherwise.
        """

        # Iterate over each row in the matrix
        for row in matrix:
            left, right = 0, len(row) - 1

            # Perform binary search on the current row
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

        # Target not found in any row
        return False
