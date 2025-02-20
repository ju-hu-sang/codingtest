N = int(input())
N_list = [list(map(int, input().split())) for _ in range(N)]
N_list
for i in sorted(N_list):
    print(i[0], i[1])