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
                # 중복이 있는 경우 (문자가 사용 되었으며, 그게 left 뒤에 있는 경우)
                left = used[s[right]] + 1
            else:
                max_len = max(max_len, right - left + 1)
            used[s[right]] = right
            
        return max_len