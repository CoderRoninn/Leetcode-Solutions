class Solution:
    def reverse(self, x: int) -> int:
        sign = +1 if x >= 0 else -1
        x = abs(x)
        max_range, min_range = (2**31)-1, -(2**31)
        reversed_number = 0

        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x //= 10

        if  min_range <=sign * reversed_number <= max_range:
            return sign * reversed_number
        else:
            return 0
              





        