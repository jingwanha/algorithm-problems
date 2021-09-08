from collections import defaultdict
import math

def solution(clothes):
    cover = defaultdict(list)
    answer = 1

    # 위장 종류를 key로 하는 dictionary 생성
    for cloth, type_ in clothes: cover[type_].append(cloth)
    for key in cover.keys():
        answer *= _combnation(len(cover[key]) + 1, 1)

    return answer - 1

def _combnation(n,r):
    return int(math.factorial(n) / (math.factorial(n-r) * math.factorial(r)))


if __name__=='__main__':
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    # clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

    res = solution(clothes)

    print(res)



