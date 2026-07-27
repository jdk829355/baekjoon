class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if (not len(nums)): return [-1, -1]

        l, u = -1, -1

        st, en = 0, len(nums)-1
        while (st < en):
            mid = (st+en)//2

            if (nums[mid] < target):
                st = mid+1
            else:
                en = mid

        if(nums[st] != target): return [-1, -1]

        l = st

        st, en = 0, len(nums)
        while (st < en):
            mid = (st+en)//2

            if (nums[mid] <= target):
                st = mid+1
            else:
                en = mid
   

        u = st-1
        return [l, u]
