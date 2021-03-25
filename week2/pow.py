class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.p(x, -n)
        return self.p(x, n)

    def p(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        return half * half * x
