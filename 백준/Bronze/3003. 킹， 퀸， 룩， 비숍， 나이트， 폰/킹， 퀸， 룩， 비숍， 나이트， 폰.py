chess_list = [1,1,2,2,2,8]
find_list = list(map(int,input().split()))
result = []
for i in range(6):
    result=chess_list[i]-find_list[i]
    print(result)