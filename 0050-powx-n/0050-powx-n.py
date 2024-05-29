class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.power(x, n)
        else:
            return 1 / self.power(x, -n)

    def power(self, i, n):
        if n == 0:
            return 1

        temp = self.power(i, n // 2)

        if n % 2 == 0:
            return temp * temp
        else:
            if n > 0:
                return i * temp * temp
            else:
                return (temp * temp) / i    