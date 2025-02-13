N, k = map(int, input().split())
stu = list(map(int, input().split()))
print(sorted(stu)[N-k])