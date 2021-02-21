# https://leetcode.com/problems/most-common-word/
import re
from collections import Counter
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pattern = '[^a-z]' # Words in the paragraph are not case sensitive.  The answer is in lowercase.

        words = re.sub(pattern, ' ', paragraph.lower())

        # words를 아래와 같이 계산할 수도 있다.
        # [\w] == word character를 의미
        # words = [word for word in re.sub('[^\w]', ' ', paragraph.lower()).split() if not word in banned]

        words_count = Counter(words.split())

        # ban words
        for ban_word in banned:
            if ban_word in words:
                words_count.pop(ban_word)

        return words_count.most_common()[0][0]

if __name__=='__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    sol = Solution()
    print(sol.mostCommonWord(paragraph,banned))
