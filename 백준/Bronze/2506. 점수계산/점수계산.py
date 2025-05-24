n = int(input())  
results = list(map(int, input().split()))  

score = 0  
current = 0  

for result in results:
    if result == 1:
        current += 1
        score += current
    else:
        current = 0  

print(score)