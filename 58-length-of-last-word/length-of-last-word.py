class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        flag = False

        for char in reversed(s):
            if char != ' ':
                length += 1
                flag = True
            elif flag:
                break
        return length            
        