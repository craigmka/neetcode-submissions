class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        tempList = nums
        left = 0
        right = len(nums) - 1

        while left <= right:
            middleIndex = (left + right)//2
            middleValue = nums[middleIndex]
            if middleValue == target:
                return middleIndex
            elif target < middleValue:
                right = middleIndex - 1
            else:
                left = middleIndex + 1
        return -1