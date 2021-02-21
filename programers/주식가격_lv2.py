def solution(prices):
    answer = []

    for i, p in enumerate(prices):
        ups = 0
        for next_p in prices[i+1:]:
            if p <= next_p : ups+=1 # 현재 값이 다음 값 보다 큰 경우
            else : continue # 작은 경우
        answer.append(ups)

    return answer

if __name__ == '__main__':
    prices = [1,1,1,1,1]

    print (solution(prices))
