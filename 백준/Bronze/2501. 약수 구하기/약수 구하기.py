N, K = map(int, input().split())
small_check = []
for i in range(1,N+1):
    if N % i == 0:
        small_check.append(i)
if len(small_check) < K :
    print(0)
else:
    print(small_check[K-1])