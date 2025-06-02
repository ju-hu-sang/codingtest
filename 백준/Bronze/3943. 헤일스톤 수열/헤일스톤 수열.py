import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    max_val = n

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        max_val = max(max_val, n)
    
    print(max_val)
