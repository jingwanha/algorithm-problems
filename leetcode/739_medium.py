# https://leetcode.com/problems/daily-temperatures/
from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        # 초기화
        result = [0]*len(T)
        tmp = [] # 임시 저장 리스트

        for i, cur_temp in enumerate(T):
            while tmp and cur_temp > T[tmp[-1]]: # 날씨가 따뜻해 졌다면
                last = tmp.pop()
                result[last] = i - last
            tmp.append(i)


        return result

if __name__=='__main__':
    T = [1,2,3,2,3]

    sol = Solution()
    print(sol.dailyTemperatures(T))
