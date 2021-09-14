# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    name = 'A' + name

    answer = 0
    for idx in range(len(name) - 1):
        # print(name[idx], name[idx + 1],
        #       abs(ord(name[idx]) - ord(name[idx + 1])) % 24,
        #       ord(name[idx + 1]) - ord('A') + 1,  # 커서 왼쪽 이동
        #       ord('Z') - ord(name[idx + 1]) + 1  # 커서 오른쪽 이동
        #       )

        answer += min(
            abs(ord(name[idx]) - ord(name[idx + 1])) % 24,  # 커서 위아래이동
            ord(name[idx + 1]) - ord('A') + 1,  # 커서 왼쪽 이동
            ord('Z') - ord(name[idx + 1]) + 1  # 커서 오른쪽 이동
        )

    return answer


name = "JAZ"
print(solution(name))