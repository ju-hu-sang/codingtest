N,X = map(int, input().split())
A = list(map(int, input().split()))
num = [i for i in A if i < X]
print(" ".join(map(str,num)))
