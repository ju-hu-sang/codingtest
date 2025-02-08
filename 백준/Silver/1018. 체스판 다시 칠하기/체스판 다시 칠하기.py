N, M = map(int, input().split())
board = [input() for _ in range(N)]
result = []
for i in range(N - 7):  
    for j in range(M - 7):
        w_start = 0  
        b_start = 0  

        for x in range(8):
            for y in range(8):
                current = board[i + x][j + y]  

                if (x+y)%2 == 0:
                    if current != 'W':
                        w_start += 1
                    if current != 'B':
                        b_start +=1
                else:
                    if current != 'B':
                        w_start +=1
                    if current != 'W':
                        b_start +=1
        result.append(w_start)
        result.append(b_start)
print(min(result))