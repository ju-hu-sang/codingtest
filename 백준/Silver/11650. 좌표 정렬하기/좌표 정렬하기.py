
N = int(input())
jum_list = [list(map(int, input().split())) for _ in range(N)]
jum_list.sort()

for x,y in jum_list:
    print(x,y)