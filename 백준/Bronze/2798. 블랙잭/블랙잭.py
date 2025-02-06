N, M = map(int, input().split())
cards = list(map(int,input().split()))

max_sum=[]
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if cards[i]+cards[j]+cards[k] <= M:
                max_sum.append(cards[i]+cards[j]+cards[k])
print(max(max_sum))