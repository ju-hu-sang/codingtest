number = [list(map(int, input().split())) for _ in range(9)]
max_num = 0
max_row, max_column = 0, 0
for i in range(9):
    for j in range(9):
        if number[i][j] >= max_num:
            max_num = number[i][j]
            max_row, max_column = i+1, j+1
print(max_num)
print(f"{max_row} {max_column}")