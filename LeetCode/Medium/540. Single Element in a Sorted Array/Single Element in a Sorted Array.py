class Solution:
    def get_up(self, nums,target):
        u = -1

        st, en = 0, len(nums)
        while (st < en):
            mid = (st+en)//2

            if (nums[mid] <= target):
                st = mid+1
            else:
                en = mid
        return st

    def singleNonDuplicate(self, nums: List[int]) -> int:
        if (len(nums) == 1): return nums[0]

        for x in nums[0::2]:
            u = self.get_up(nums, x)
            if nums[u-1] != nums[u-2]:
                return x
