voca = input()
croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']
croa_voca = []
for i in croa:
    voca = voca.replace(i,"0")
print(len(voca))