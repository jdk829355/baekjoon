class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        if N < 2:
            return N

        left = 0
        used = {}
        max_len = 0

        for right in range(N):
            if s[right] in used and left <= used[s[right]]:
                    left = used[s[right]] + 1
                    used[s[right]] = right
            else:
                used[s[right]] = right
                max_len = max(max_len, right - left + 1)
        return max_len