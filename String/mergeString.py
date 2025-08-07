class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1, w2 = 0, 0  # Initialize pointers for both words
        result = ''    # Initialize the result string

        # Add characters alternately from both strings until one is exhausted
        while w1 < len(word1) and w2 < len(word2):
            result += word1[w1] + word2[w2]
            w1 += 1
            w2 += 1

        # Append remaining characters from word1, if any
        while w1 < len(word1):
            result += word1[w1]
            w1 += 1

        # Append remaining characters from word2, if any
        while w2 < len(word2):
            result += word2[w2]
            w2 += 1

        return result
