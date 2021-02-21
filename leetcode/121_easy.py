# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price) # 현재 기준 최소값 계산
            max_profit = max(max_profit,price-min_price) # 현재 기준 최소값에서 현재 값의 차이 중 큰 값

        return max_profit

if __name__=='__main__':
    prices = [7,1,5,3,6,4]

    sol = Solution()
    print (sol.maxProfit(prices))
