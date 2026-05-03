class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {')': '(', '}': '{', ']': '['}
        stack = []

        for val in s:
            if val in bracket.values():  # opening bracket
                stack.append(val)
            else:  # closing bracket
                if not stack or stack[-1] != bracket[val]:
                    return False
                stack.pop()

        # stack should be empty if all brackets matched
        return not stack