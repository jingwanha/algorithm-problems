# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True

    sorted_phone_book = sorted(phone_book)

    for idx, number in enumerate(sorted_phone_book[:-1]):
        next_number = sorted_phone_book[idx + 1]
        if (len(number) <= len(next_number)) and (number == next_number[:len(number)]):
            answer=False

            return answer

    return answer


if __name__=='__main__':
    phone_book = ["119", "97674223", "1195524421"]

    res = solution(phone_book)
    print(res)



