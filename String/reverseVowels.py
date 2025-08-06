class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        chars = list(s)
        l, r = 0, len(chars) - 1
        
        while l < r:
            if chars[l] in vowels and chars[r] in vowels:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
            elif chars[l] in vowels:
                r -= 1
            else:
                l += 1
        
        return "".join(chars)