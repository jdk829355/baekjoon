class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        k = 0
        n = len(nums)

        for i in range(n):
            next = (i+1)%n
            if nums[next] < nums[i]:
                k = next
                break

        nums_sorted = [nums[(i+k)%n] for i in range(n)] 
        st, en = 0, n-1

        while (st <= en):
            mid =(st+en)//2
            num = nums_sorted[mid]

            if num == target: return (mid+k)%n

            if num < target:
                st = mid+1
            else:
                en = mid-1

        return -1
