# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []

    for i, f_num in enumerate(numbers):
        for s_num in numbers[i + 1:]:
            answer.append(f_num + s_num)

    answer = list(set(answer))
    answer.sort()

    return answer