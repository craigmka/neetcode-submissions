class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False

        stack = []

        for char in s:
            if char == ")":
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif char == "}":
                if not stack or stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            elif char == "]":
                if not stack or stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        if stack:
            return False
        return True