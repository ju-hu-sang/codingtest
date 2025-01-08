alpha = input().upper()
alpha_count = {}
for i in alpha:
    if i in alpha_count:
        alpha_count[i]+=1
    else:
        alpha_count[i]=1
max1 = max(alpha_count.values())
key_1 = [i for i,j in alpha_count.items() if j == max1]
if len(key_1) ==1:
    print(key_1[0])
else:
    print('?')