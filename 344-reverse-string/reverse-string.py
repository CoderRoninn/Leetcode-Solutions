class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)

        for i in range(length // 2):
            s[i], s[length-1-i] = s[length-1-i], s[i]

        

        
        
        