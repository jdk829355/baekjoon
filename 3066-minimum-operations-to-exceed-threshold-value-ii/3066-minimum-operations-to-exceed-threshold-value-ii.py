class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        import heapq as hq
        hq.heapify(nums)

        cnt = 0
        while len(nums) > 1:
            left = hq.heappop(nums)
            right = hq.heappop(nums)

            if left >= k:
                return cnt
            
            new = min(left, right) * 2 + max(left, right)
            hq.heappush(nums, new)
            cnt += 1

        return cnt