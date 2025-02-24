class Solution:
    def calculate(self, s: str) -> int:
        result = []
        sign = "+"
        num = 0
       

        for i,op in enumerate(s):
            if op.isdigit():
                num = num * 10 + int(op)

            if op in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    result.append(num)
                elif sign == "-":
                    result.append(-num)
                elif sign == "*":
                    result[-1] = result[-1] * num
                elif sign == "/":
                    result[-1] = int(result[-1] / num)  
                sign = op
                num = 0      
        return sum(result)

            

        
        