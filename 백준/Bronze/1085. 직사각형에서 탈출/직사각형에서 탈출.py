x,y,w,h = map(int, input().split())
four_list = [h-y,y,x,w-x]
print(min(four_list))