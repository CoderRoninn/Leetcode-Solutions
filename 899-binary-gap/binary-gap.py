class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        prev = -1
        max_distance = 0

        for i, bit in enumerate(binary):
            if bit == '1':
                if prev != -1:
                    max_distance = max(max_distance, i-prev)
                prev = i
        return max_distance        
        