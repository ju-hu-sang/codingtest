A, B = map(int, input().split())
C = int(input())
D = 60*A + B + C
A = D//60 
B = D %60
if A>23:
    print(A-24, B)
else:
    print(A, B)