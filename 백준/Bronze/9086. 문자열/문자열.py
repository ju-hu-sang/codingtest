T = int(input())
for _ in range(T):
    test_str = list(map(str, input()))
    test_str1 = [test_str[0],test_str[-1]]
    print(''.join(test_str1))