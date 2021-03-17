# https://leetcode.com/problems/jewels-and-stones/

from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0

        cnt = Counter(stones)
        for jewle in jewels:
            result+=cnt[jewle]

        return result


if __name__=='__main__':
    jewels = "aA"
    stones = "aAAbbbb"

    sol = Solution()
    result = sol.numJewelsInStones(jewels,stones)

    print (result)
