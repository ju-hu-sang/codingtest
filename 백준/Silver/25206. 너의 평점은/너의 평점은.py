rank_dic = {"A+": 4.5,
            "A0": 4.0,
            'B+' : 3.5,
            'B0' : 3.0,
            'C+' : 2.5,
            'C0' : 2.0,
            'D+' : 1.5,
            'D0' : 1.0,
            'F' : 0}
total_hak = 0
total_rank_hak = 0
for _ in range(20):
    subject, hak, rank = input().split()
    hak = float(hak)

    if rank == "P":
        continue
    if rank in rank_dic :
        total_hak += hak
        total_rank_hak += hak*rank_dic[rank]

avg = total_rank_hak/total_hak

print(f"{avg:.4f}")