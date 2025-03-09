class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor_sum = 0

        for char in s:
            xor_sum ^= ord(char)
        for char in t:
            xor_sum ^= ord(char)
        return chr(xor_sum)        
        