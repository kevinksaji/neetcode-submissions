class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_f = 0
        start = 0
        max_length = 0

        for end in range(len(s)):

            count[s[end]] = 1 + count.get(s[end], 0)

            max_f = max(max_f, count[s[end]])

            while (end - start + 1) - max_f > k:
                count[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length

        
