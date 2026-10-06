class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []

        if len(s) < 4 or len(s) > 12:
            return res

        def backtrack(index: int, parts: List[str]) -> None:
            if len(parts) == 4:
                if index == len(s):
                    res.append(".".join(parts))
                return

            remaining_chars = len(s) - index
            remaining_parts = 4 - len(parts)

            # Pruning
            if remaining_chars < remaining_parts:
                return
            if remaining_chars > remaining_parts * 3:
                return

            for j in range(index, min(index + 3, len(s))):
                part = s[index:j + 1]

                # Leading zeros are not allowed
                if len(part) > 1 and part[0] == '0':
                    continue

                if int(part) <= 255:
                    parts.append(part)
                    backtrack(j + 1, parts)
                    parts.pop()

        backtrack(0, [])
        return res