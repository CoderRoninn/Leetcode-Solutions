class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_odd, sum_even = 0, 0

        sum_odd = sum(number for number in nums if number <= 9)
        sum_even = sum(number for number in nums if 10 <= number)

        if sum_odd != sum_even:
            return True
        return False    
        
        