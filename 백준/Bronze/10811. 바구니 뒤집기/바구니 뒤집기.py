N, M = map(int, input().split())
baguni_num = list(range(1,N+1))
# M번반복
for _ in range(M):
    i,j = map(int, input().split())
    baguni_num[i-1:j] = baguni_num[i-1:j][::-1]
print(' '.join(map(str, baguni_num)))