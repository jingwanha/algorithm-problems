# https://leetcode.com/problems/array-partition-i/

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n_num = len(nums)
        total_sum = 0

        # 정렬 후 차례로 두 개 씩 묶음
        nums.sort()
        for i in range(0, n_num, 2):
            total_sum += min(nums[i], nums[i + 1])

        return total_sum

        # 아래와 같이 한 줄로도 풀이가 가능
        # return sum(sorted(nums)[::2])


if __name__=='__main__':
    nums = [6, 2, 6, 5, 1, 2]

    sol = Solution()
    print (sol.arrayPairSum(nums))