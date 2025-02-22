class Solution:
    def secondHighest(self, s: str) -> int:
        digits = {int(number) for number in s if number.isdigit()}

        if len(digits) < 2:
            return -1

        return max(x for x in digits if x < max(digits))    
        