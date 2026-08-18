class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        N = len(nums)
        res = set()
        
        for i in range(N-2):
            st = i+1
            en = N-1

            while st < en:
                s = nums[st] + nums[en] + nums[i]
                
                if s == 0:
                    res.add(tuple(sorted([nums[st], nums[en], nums[i]])))
                    st += 1
                    en -= 1
                elif s > 0:
                    en -= 1
                else:
                    st += 1

        return list(res)