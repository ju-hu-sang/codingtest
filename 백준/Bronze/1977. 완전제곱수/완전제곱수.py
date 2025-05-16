import math
import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
squares = [k * k for k in range(math.isqrt(M), math.isqrt(N) + 1) if M <= k * k <= N]

if not squares:            
    print(-1)
else:
    print(sum(squares))      
    print(squares[0])        
