class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_string = "".join(c.lower() for c in s if c.isalnum())
        return my_string == my_string[::-1]
        