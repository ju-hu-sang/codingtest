import sys
input = sys.stdin.readline 

n,m = map(int, input().split())
number = list(map(int, input().split()))

array1 = [0]*(n+1)
for i in range(1,n+1):
    array1[i] = array1[i-1] + number[i-1]

for _ in range(m):
    i,j = map(int, input().split())
    print(array1[j]-array1[i-1])