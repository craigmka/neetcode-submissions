class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        tempArray = ""

        for char in s:
            if char.isalnum():
                tempArray += char.lower()

        pointer1 = 0
        pointer2 = len(tempArray)-1

        while pointer1 < pointer2:
            if tempArray[pointer1] != tempArray[pointer2]:
                return False
            pointer1 += 1
            pointer2 -= 1

        return True