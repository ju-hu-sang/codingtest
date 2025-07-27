def solution(rank, attendance):
    true_list = []
    for i in range(len(rank)):
        if attendance[i]:
            true_list.append((rank[i], i))
    true_list.sort()
    a,b,c = true_list[0][1],true_list[1][1],true_list[2][1]
    return 10000*a + 100*b + c