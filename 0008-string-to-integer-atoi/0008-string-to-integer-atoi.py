class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Sign
        sign = 1

        if i < n and s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i += 1

        # Build number
        result = 0

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")

            result = result * 10 + digit
            i += 1

        result *= sign

        # 32-bit integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if result < INT_MIN:
            return INT_MIN

        if result > INT_MAX:
            return INT_MAX

        return result