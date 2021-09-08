# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import defaultdict


# # 베스트 솔루션
# import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]


def solution(participant, completion):
    # dict 자료형으로 변경
    ans = ''

    participant_dict = defaultdict(int)
    for p_name in participant: participant_dict[p_name] += 1

    for c_name in completion:
        participant_dict[c_name] -= 1

    for key in participant_dict.keys():
        if participant_dict[key] == 1:
            ans = key

    return ans

if __name__=='__main__':
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]

    res = solution(participant,completion)
    print(res)