class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        chars = set(c for c in s)
        
        def solve_n(n):
            chars_map = {
                c: 0 for c in chars
            }

            for c in s[:n]:
                chars_map[c] += 1
        
            if len(set(s[:n])) == n: return True

            left, right = 0, n-1
            
            while right+1 < len(s):
                chars_map[s[left]] -= 1
                chars_map[s[right+1]] += 1

                if chars_map[s[left]]==1 and len(set(s[left+1:right+2])) == n: return True

                left += 1
                right += 1
            
            return False
        
        st, en = 1, len(s)

        while st < en:
            mid = max((st+en)//2, (st+en+1)//2)
            res = solve_n(mid)

            if res:
                st = mid
            else:
                en = mid-1
        
        return st