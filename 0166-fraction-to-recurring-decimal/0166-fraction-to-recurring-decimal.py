class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # If numerator is 0
        if numerator == 0:
            return "0"

        result = []

        # Handle negative result
        if (numerator < 0) != (denominator < 0):
            result.append("-")

        # Work with positive numbers
        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        result.append(str(numerator // denominator))

        remainder = numerator % denominator

        # No fractional part
        if remainder == 0:
            return "".join(result)

        result.append(".")

        # remainder -> position in result
        seen = {}

        while remainder != 0:

            # Repeating remainder found
            if remainder in seen:
                pos = seen[remainder]
                result.insert(pos, "(")
                result.append(")")
                break

            # Remember where this remainder starts
            seen[remainder] = len(result)

            remainder *= 10

            result.append(str(remainder // denominator))

            remainder %= denominator

        return "".join(result)