class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        n = len(s)

        if n < word_len * word_count:
            return []

        need = Counter(words)
        res = []

        for offset in range(word_len):
            left = offset
            count = 0
            seen = {}

            for right in range(offset, n - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in need:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    while seen[word] > need[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == word_count:
                        res.append(left)

                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    seen.clear()
                    count = 0
                    left = right + word_len

        return res