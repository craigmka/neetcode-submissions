class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        tempArray = []

        for i in range(len(s)):
            if s[i].isalnum():
                tempArray.append(s[i].lower())

        pointer1 = 0
        pointer2 = len(tempArray)-1

        while pointer1 < pointer2:
            if tempArray[pointer1] != tempArray[pointer2]:
                return False
            else:
                pointer1 += 1
                pointer2 -= 1

        return True