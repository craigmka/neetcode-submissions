class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        repeated = []

        for num in nums:
            if num in repeated:
                return True
            repeated.append(num)
        
        return False