# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]

        # 왼쪽 요소들의 곱
        for i in range(1, len(nums)):
            output.append(output[i - 1] * nums[i - 1])

        p = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] = output[i]*p # 왼쪽 요소들의 곱 * 오른쪽 요소들의 곱
            p = p*nums[i] # 오른쪽 요소들의 곱을 계속 저장

        return  output

if __name__=='__main__':
    nums = [1,2,3,4]

    sol = Solution()
    print (sol.productExceptSelf(nums))