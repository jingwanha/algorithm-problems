def solution(board, moves):

    answer = 0
    pockets = [0] # 마지막 인덱스를 확인하기 위하여 0으로 초기화
    n_board = len(board)

    for move in moves:
        for i in range(n_board):
            if board[i][move - 1] != 0:

                if pockets[-1] == board[i][move - 1]:
                    pockets.pop()
                    answer += 2

                else:
                    pockets.append(board[i][move - 1])

                board[i][move - 1] = 0
                break

    return answer


if __name__=='__main__':
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]

    print(solution(board,moves))