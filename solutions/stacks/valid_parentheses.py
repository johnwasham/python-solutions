"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([])"
Output: true

Input: s = "([)]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matches = {
            '[': ']',
            '{': '}',
            '(': ')',
        }

        for c in s:
            if c in matches:  # it's an opener
                stack.append(c)
            else:  # it's a closer
                if not stack:
                    return False
                else:
                    if matches[stack[-1]] == c:
                        stack.pop()
                    else:
                        return False

        return len(stack) == 0

sol = Solution()
assert sol.isValid("()") == True
assert sol.isValid("()[]{}") == True
assert sol.isValid("((]))") == False