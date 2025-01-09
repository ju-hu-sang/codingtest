count = int(input())
group_count = 0
for _ in range(count):
    voca = input()
    seen = []
    last = ""
    group = True

    for i in voca:
        if i != last:
            if i in seen:
                group=False
                break
            seen.append(i)
            last = i
    if group:
        group_count+=1
print(group_count)