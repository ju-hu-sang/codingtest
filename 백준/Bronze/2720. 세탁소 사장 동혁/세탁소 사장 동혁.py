T = int(input())
quater = 0 
dime = 0
nikel = 0
penny = 0
for _ in range(T):
    C = int(input())
    quater = C//25
    dime = C%25//10
    nikel = C%25%10//5
    penny = str(C%25%10%5)
    print(quater, dime, nikel, penny) 