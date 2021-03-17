# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        cur_idx = 0
        before_char = {}

        for idx, char in enumerate(s):

            # 이전에 나온 단어가 등장하면
            if char in before_char and cur_idx <= before_char[char]:
                cur_idx = before_char[char] + 1  # 동일 단어의 인덱스 위치 다음으로 이동

            else:
                max_length = max(max_length, idx - cur_idx + 1)

            # 단어의 마지막 인덱스 저장
            before_char[char] = idx

        return max_length

if __name__=='__main__':
    s = "abcabcbb"

    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)

    print (result)

