class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        result = []

        for token in tokens:
            if token not in "+*/-":
                result.append(int(token))  
            else:
                x = result.pop()
                y = result.pop()
                if token == "+":
                    result.append(x + y)
                elif token == "-":
                    result.append(y- x)
                elif token == "*":
                    result.append(x * y)
                elif token == "/":
                    result.append(int(y / x))  
        return result[0]                 
                



        