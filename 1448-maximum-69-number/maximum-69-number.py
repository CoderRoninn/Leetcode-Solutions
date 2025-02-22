class Solution:
    def maximum69Number (self, num: int) -> int:

        str_number = str(num)
        str_number =  str_number.replace('6', '9', 1)

        return int(str_number)

        