class Solution:
    def isValid(self, s: str) -> bool:

        corresponding = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []

        for char in s:
            if char in corresponding:
                if stack and stack[-1] == corresponding[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0