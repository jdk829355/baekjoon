class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        st, en = 0, k-1
        s = sum(nums[st:en+1])
        max_s = s

        while en+1 < len(nums):
            new_s = s-nums[st]+nums[en+1]
            max_s = max(max_s, new_s)
            s = new_s
            st, en = st+1, en+1
        
        return max_s/k