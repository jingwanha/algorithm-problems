# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Brute-Force로 풀이
        for first_idx, first_num in enumerate(nums):
            for second_idx, second_num in enumerate(nums[first_idx+1:]):
                if first_num + second_num  == target:
                    return  [first_idx,  second_idx+first_idx +  1] # exactly one solution


if __name__=='__main__':
    nums =   [2,7,11,15]
    target =  9

    sol = Solution()
    result = sol.twoSum(nums,target)

    print(result)