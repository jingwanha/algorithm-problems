# https://programmers.co.kr/learn/courses/30/lessons/42586

import math

def solution(progresses, speeds):
    answer = []

    # 기능 별 개발이 완료되는 시간 계
    deploy_days = [math.ceil((100 - p)/s) for p, s in zip(progresses, speeds)]

    cur_day = deploy_days.pop(0)
    cnt = 1
    while deploy_days:
        # 다음 기능의 완료가 빨리 되
        if cur_day >= deploy_days[0]:
            deploy_days.pop(0)
            cnt += 1

        else:
            cur_day = deploy_days.pop(0)
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)

    return answer

if __name__=='__main__':

    progresses = [93, 30, 55]
    speeds = 	[1,30,5]

    res = solution(progresses,speeds)
    print(res)
