N = int(input())
M_min = 0
for M in range(max(1,N-9*len(str(N))),N):
    M_sum = sum(map(int, str(M)))
    if M + M_sum == N:
        M_min = M
        break
print(M_min)