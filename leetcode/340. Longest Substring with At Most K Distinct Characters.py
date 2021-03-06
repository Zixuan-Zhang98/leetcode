class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        freq = {}
        result = 0
        left = 0
        for right in range(len(s)):
            c = s[right]
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
            while len(freq) > k:
                c = s[left]
                freq[c] -= 1
                if freq[c] == 0:
                    del freq[c]
                left += 1
            result = max(result, right - left + 1)
        return result