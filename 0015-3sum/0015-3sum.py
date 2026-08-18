class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        N = len(nums)
        res = set()
        
        
        for i in range(N-2):
            if i>0 and nums[i-1] == nums[i]:
                continue

            st = i+1
            en = N-1
            visited = set()

            while st < en:
                if tuple([nums[st], nums[en]]) in visited:
                    st += 1
                    en -= 1
                    continue

                s = nums[st] + nums[en] + nums[i]
                
                if s == 0:
                    res.add(tuple([nums[i], nums[st], nums[en]]))
                    visited.add(tuple([nums[st], nums[en]]))
                    st += 1
                    en -= 1
                elif s > 0:
                    en -= 1
                else:
                    st += 1

        return list(res)