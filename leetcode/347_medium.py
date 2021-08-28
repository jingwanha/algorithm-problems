# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        cnt = Counter(nums)

        for val,_ in cnt.most_common(k):
            result.append(val)

        return result

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    sol = Solution()
    result = sol.topKFrequent(nums,k)

    print(result)