num1 = list(int(input()) for _ in range(10))
num1_lst = []
for i in num1:
    j = i%42
    num1_lst.append(j)
print(len(set(num1_lst)))