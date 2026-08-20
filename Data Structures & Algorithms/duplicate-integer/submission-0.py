class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsRepeat = []
        for i in nums:
            if i in numsRepeat:
                return True
            numsRepeat.append(i)
        return False