S = input()
lst = []
dane = "abcdefghijklmnopqrstuvwxyz"
for dn in dane:
    if dn in S:
        lst.append(str(S.index(dn)))
    else:
        lst.append('-1')
print(' '.join(lst))