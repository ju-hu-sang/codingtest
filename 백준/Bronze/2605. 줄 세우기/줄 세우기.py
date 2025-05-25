n = int(input())
moves = list(map(int, input().split()))

queue = []

for i in range(n):
    student = i + 1  
    idx = len(queue) - moves[i]
    queue.insert(idx, student)

print(' '.join(map(str, queue)))
