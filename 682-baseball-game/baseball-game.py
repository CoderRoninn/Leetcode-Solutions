class Solution:
    def calPoints(self, operations: List[str]) -> int:
        keep_record = []

        for op in operations:
            if op == '+':
                keep_record.append(keep_record[-1] + keep_record[-2])
            elif op == 'D':
                keep_record.append(2 * keep_record[-1])  
            elif op == 'C':
                keep_record.pop()
            else:
                keep_record.append(int(op))
        return sum(keep_record)        
                 
        
        