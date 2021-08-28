# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    for completion_name in completion:
        participant.remove(completion_name)
    answer = participant[0]

    return answer

if __name__=='__main__':
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]

    res = solution(participant,completion)
    print(res)