# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):

    # 정답 초기화
    answer = []
    for i in range(len(prices), 0, -1): answer.append(i - 1)

    # 인덱스가 저장될 임시 리스트
    tmp = []

    for i, cur_price in enumerate(prices):
        while tmp and cur_price < prices[tmp[-1]]: # 가격이 떨어지면
            last = tmp.pop()
            answer[last] = i-last
        tmp.append(i) # 가격이 떨이지지 않으면 해당 인덱스를 저장

    return answer

if __name__ == '__main__':
    prices = [5,4,3,2,1]
    print (solution(prices))