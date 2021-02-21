# https://leetcode.com/problems/reverse-string/
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:

        # Do not allocate extra space for another array,
        # you must do this by modifying the input array in -place with O(1) extra memory.

        # print(s[::-1]) # Leetcode 플랫폼에서는 동작하지 않는 방식

        s.reverse()
        print (s)



if __name__=='__main__':
    input_arr =  ["h", "e", "l", "l", "o"]

    sol = Solution()
    sol.reverseString(input_arr)
