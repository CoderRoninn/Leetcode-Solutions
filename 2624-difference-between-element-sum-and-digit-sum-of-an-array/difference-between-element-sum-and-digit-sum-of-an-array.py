class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        sum, sum_digit = 0, 0

        for number in nums:
            sum += number
            if number <= 9:
                sum_digit += number
            else:
                while number > 0:
                    sum_digit += number % 10
                    number //= 10        
        return abs(sum - sum_digit)            
        