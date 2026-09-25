class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)
        a, b = abs(dividend), abs(divisor)

        ans = 0
        while a >= b:
            shift = a.bit_length() - b.bit_length()
            if (b << shift) > a:
                shift -= 1

            ans += 1 << shift
            a -= b << shift

        return -ans if negative else ans