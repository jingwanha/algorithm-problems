# https://programmers.co.kr/learn/courses/30/lessons/42587

from typing import List

def solution(priorities:List[int], location:int)->int:

    answer = 0
    max_val = max(priorities)

    cnt = 0
    while priorities:
        # 출력 대상인 경우
        if priorities[0] >= max_val:
            priorities.pop(0)  # 출력 한 후
            cnt+=1

            # 출력한 것이 target 이면
            if location == 0:
                answer = cnt
                break

            if priorities: max_val = max(priorities)
            location -= 1

        # 출력 대상이 아닌 경우
        elif priorities[0] < max_val:
            # 현재 출력대상을 맨 뒤로 이동
            priorities.append(priorities.pop(0))

            # 현재 출력 대상이 location면 맨 뒤 인덱스로 아니면 현재 위치에서 -1
            location = len(priorities) - 1 if location == 0 else location - 1

    return answer


if __name__=='__main__':
    priorities = [2,1,3,2]
    location = 2

    res = solution(priorities,location)
    print(res)