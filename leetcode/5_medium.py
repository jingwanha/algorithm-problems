class Solution:
    def longestPalindrome(self, s: str) -> str:

        len_s = len(s)
        # 문자열 길이 부터 -1 하면서 가장 긴 Palindrome 탐색
        for i in range(len_s, 0, -1):
            for j in range(len_s):
                if j + i > len_s: break

                if self._is_palinfromic(s[j:j + i]):
                    return s[j:j + i] # 무조건 존재하므로 return

    def _is_palinfromic(self, s : str)->bool:
        return s==s[::-1]

if __name__=='__main__':
    s = "babad"

    sol = Solution()
    print (sol.longestPalindrome(s))

