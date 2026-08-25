class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            middleIndex = (left + right)//2
            if target == nums[middleIndex]:
                return middleIndex
            elif target < nums[middleIndex]:
                right = middleIndex - 1
            else:
                left = middleIndex + 1
        return -1