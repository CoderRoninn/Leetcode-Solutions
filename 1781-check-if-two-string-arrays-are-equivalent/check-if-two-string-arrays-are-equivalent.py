class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        str1 = ''.join(word1)
        str2 = ''.join(word2)

        if len(str1) != len(str2):
            return False

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
        return True            
        