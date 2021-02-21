# https://leetcode.com/problems/reorder-data-in-log-files/

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        # 각각 숫자 로그 문자열 로그를 분리해서 정렬한 뒤 병합
        char_logs = []
        digit_logs = []

        for log in logs:
            if log.split(' ')[1].isdigit():
                digit_logs.append(log)
            else:
                char_logs.append(log)

        # 정렬 기준이 두 개
        # the logs so that all of the letter-logs come before any digit-log
        # The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties
        # The digit-logs should be put in their original order.

        # 뒤의 로그가 동일하면 identifier 순으로 정렬
        sorted_char_logs = sorted(char_logs, key=lambda log: (log.split(' ')[1:], log[0]))

        return sorted_char_logs + digit_logs

if __name__=='__main__':
    logs = ["j mo", "5 m w", "g 07", "o 2 0", "t q h"]

    sol = Solution()
    print(sol.reorderLogFiles(logs))

