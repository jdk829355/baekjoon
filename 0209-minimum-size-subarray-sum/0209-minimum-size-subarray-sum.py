class Solution:
    def is_gte_target(self, nums, n, target):
        left, right = 0, n-1
        s = sum(nums[left:right+1])
        if s >= target: return True

        while right+1 < len(nums):
            s = s - nums[left] + nums[right+1]
            if s >= target: return True

            left, right = left+1, right+1

        return False


    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        N = len(nums)

        st, en = 1, N

        while st < en:
            mid = (st+en)//2
            
            if self.is_gte_target(nums, mid, target):
                en = mid
            else:
                st = mid+1

        return st