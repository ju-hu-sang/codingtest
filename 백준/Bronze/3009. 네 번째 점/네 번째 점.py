a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
list1 = [a,c,e]
list2 = [b,d,f]
list3 = []
for i in list1:
    if list1.count(i) == 1:
        list3.append(i)
for i in list2:
    if list2.count(i) == 1:
        list3.append(i)

print(list3[0], list3[1])