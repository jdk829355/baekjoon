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

            while st < en:

                s = nums[st] + nums[en] + nums[i]
                
                if s == 0:
                    res.add(tuple([nums[i], nums[st], nums[en]]))
                    st += 1
                    en -= 1
                    while st < en and st > 0 and en < N-1:
                        if nums[st-1] == nums[st]: 
                            st += 1 
                        else: 
                            break
                        if nums[en+1] == nums[en]: 
                            en -= 1 
                        else: 
                            break

                elif s > 0:
                    en -= 1
                else:
                    st += 1

        return list(res)