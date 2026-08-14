class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers = [-1001]+numbers
        
        left, right = 1, len(numbers)-1

        while left < right:
            s = numbers[left] + numbers[right]

            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                return [left, right]