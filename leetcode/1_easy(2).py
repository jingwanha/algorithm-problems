# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 'in' 연산자와 dictionary를 이용하여 풀이
        # Brute-Force 풀이보다 훨씬 속도가 빠름

        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num] = i

        for i , num in enumerate(nums):
            if target - num in nums_dict and i != nums_dict[target-num]: # 자기 자신과 더해지는 경우 제
                return nums.index(num), nums_dict[target-num] # exactly one solution


if __name__=='__main__':
    nums =   [3,3,4,5,6,7]
    target =  6

    sol = Solution()
    result = sol.twoSum(nums,target)

    print(result)