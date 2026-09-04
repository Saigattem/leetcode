class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total_sum = 0
        sign = 1
        digits = []

        while n > 0:
            digits.append(n % 10)
            n //= 10

        digits.reverse()

        for d in digits:
            total_sum += d * sign
            sign = -sign

        return total_sum