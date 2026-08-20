class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        repeated = {}

        for num in nums:
            if num in repeated:
                return True
            else:
                repeated[num] = True    
        return False