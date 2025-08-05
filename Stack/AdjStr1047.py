class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Time Complexity: O(n), where n is the length of the input string.
        # Space Complexity: O(n), for storing characters in the stack.
        stack = []

        for char in s:
            # If the current character matches the last one in the stack, pop it
            if stack and stack[-1] == char:
                stack.pop()
            else:
                # Otherwise, push the character onto the stack
                stack.append(char)

        # Join the remaining characters in the stack to form the result
        return ''.join(stack)
