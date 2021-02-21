# https://leetcode.com/problems/group-anagrams/
from typing import List

class Solution:
    # 첫 풀이 방법
    # 수행시간이 n제곱이기 때문에 Time Limit Exceeded 에러 발생
    # defaultdict를 이용하여 n 시간만에 풀이 가능
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []

        while strs:
            word = strs.pop()
            group = []

            for s in strs:
                if ''.join(sorted(s)) == ''.join(sorted(word)): # 문자열을 정렬하여 동일한지 비교
                    group.append(s)

            if group:
                for g in group : strs.remove(g)

            group.append(word)
            anagrams.append(group)

        return anagrams


if __name__=='__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]

    sol = Solution()
    print(sol.groupAnagrams(strs))