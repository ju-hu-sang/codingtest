# 먼저 입력받은값들의 리스트를 내림차순정렬해야함
# 금액 k와 count 

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin1 = sorted(coin,reverse=True)

count = 0
for i in coin1:
    count = count + k//i
    k = k%i

print(count)