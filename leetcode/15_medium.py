# https://leetcode.com/problems/3sum/
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # 정렬 후 two 포인터 이용
        nums.sort()
        sum_zero = []

        for idx, num in enumerate(nums):
            left_idx, right_idx = idx + 1, len(nums) - 1

            while left_idx < right_idx: # 탈출 조건

                if num + nums[left_idx] + nums[right_idx] == 0: #합이 0인경우 리스트에 추가 + 인덱스 변경
                    sum_zero.append([num, nums[left_idx], nums[right_idx]])
                    left_idx+=1
                    right_idx-=1

                elif num + nums[left_idx] + nums[right_idx] < 0: #0보다 작은경우 더한 합이 커지게 하기 위해 leff_idx를 우측으로 이동
                    left_idx += 1

                else: # 합이 0보다 큰 경우 합이 작아지게 하기 위하여 right_idx를 왼쪽으로 이동
                    right_idx -= 1


        # 중복제거
        result = []
        for sum_idx in sum_zero:
            if sum_idx not in result: result.append(sum_idx)

        return result

if __name__=='__main__':
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [-2,0,1,1,2]

    sol = Solution()
    print (sol.threeSum(nums))


