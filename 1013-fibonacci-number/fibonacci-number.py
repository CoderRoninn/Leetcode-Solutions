class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        t1, t2, next = 0, 1, 0

        for i in range(2, n+1):
            next = t1 + t2
            t1 = t2
            t2 = next
        return next
        
        