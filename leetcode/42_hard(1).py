# https://leetcode.com/problems/trapping-rain-water/
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n_rain = 0
        n_height = len(height)

        for idx, h in enumerate(height[1:n_height - 1]):

            # height의 요소 수가 커질 수록 max를 계산하는 시간이 늘어남
            # 투 포인터를 이용하여 매번 max를 계산하지 않도록 할 수 있

            left_max = max(height[:idx + 1])
            right_max = max(height[idx + 2:])

            if min(left_max, right_max) >= h:  # 현재 값이 좌우 최댓 값 중 작은 값보다 작을 때만
                min_val = min(left_max, right_max)

                n_rain += (min_val - h)  # 물방울 수 count
                height[idx + 1] += (min_val - h)  # 물방울로 빈 곳 채우기

        return n_rain


if __name__ == '__main__':
    height = [4, 2, 0, 3, 2, 5]

    sol = Solution()
    print(sol.trap(height))
