N, M = map(int, input().split())
baguni = [k for k in range(1,N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    baguni[i-1], baguni[j-1] = baguni[j-1], baguni[i-1]
    
print(" ".join(map(str, baguni))) 