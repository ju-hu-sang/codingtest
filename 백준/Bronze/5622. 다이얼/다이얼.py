A = input()
diel_dic = {3:'ABC',4:'DEF',5:'GHI',6:'JKL',7:'MNO',8:'PQRS',9:'TUV',10:'WXYZ'}
time1 = 0
for i in A:
    for key, value in diel_dic.items():
        if i in value:
            time1+=key
print(time1)