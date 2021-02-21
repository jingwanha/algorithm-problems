# https://leetcode.com/problems/valid-palindrome/
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = '[^a-z0-9]' # considering only alphanumeric characters and ignoring cases.

        s = s.lower()
        s = re.sub(pattern,'',s)

        reverse_s = s[::-1]

        return s==reverse_s

if __name__=='__main__':
    sol = Solution()

    input = "A man, a plan, a canal: Panama"
    print (sol.isPalindrome(input))