# https://leetcode.com/problems/group-anagrams/
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # list 자료형을 default로 가지는 dict 자료형 생성

        # 수행시간 n만에 해결 가능
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values()) # You can return the answer in any order.


if __name__=='__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]

    sol = Solution()
    print(sol.groupAnagrams(strs))
