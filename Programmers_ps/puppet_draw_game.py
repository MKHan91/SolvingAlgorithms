def solution(board, moves):
    answer = 0
    basket = []
    column_list = []
    for k in range(len(board)):
        row_list = []
        for n in range(len(board)):
            if board[n][k] != 0:
                row_list.append(board[n][k])
        column_list.append(row_list)
    
    for pos in moves:
        if sum(column_list[pos-1]) == 0: continue
        basket.append(column_list[pos-1].pop(0))
        if len(basket) > 1:
            if basket[-1] == basket[-2]:
                for _ in range(2):
                    del basket[-1]
                answer += 2
    return answer

def solution2(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution2(board, moves))