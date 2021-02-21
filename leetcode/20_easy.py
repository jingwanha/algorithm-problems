# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:

        pair_dict = {')' : '(',
                     '}' : '{',
                     ']' : '['}

        stack = []
        for bracket in s:
            if bracket in pair_dict.values():
                stack.append(bracket)
            else:
                if stack and stack[-1] == pair_dict[bracket]:
                    stack.pop()
                else: return False

        # 남아있는 경우 False
        if stack: return False

        return True

if __name__=='__main__':
    s ="]"

    sol = Solution()
    print (sol.isValid(s))

