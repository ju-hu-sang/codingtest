def is_consonant(c):
    return c not in 'aeiou'

def count_n_value(name, n):
    L = len(name)
    total = 0
    cons_len = 0
    last_valid = -1

    for i in range(L):
        if is_consonant(name[i]):
            cons_len += 1
        else:
            cons_len = 0
        
        if cons_len >= n:
            last_valid = i - n + 1
        if last_valid != -1:
            total += last_valid + 1  

    return total

T = int(input())
for case_num in range(1, T + 1):
    parts = input().split()
    name = parts[0]
    n = int(parts[1])
    result = count_n_value(name, n)
    print(f"Case #{case_num}: {result}")
