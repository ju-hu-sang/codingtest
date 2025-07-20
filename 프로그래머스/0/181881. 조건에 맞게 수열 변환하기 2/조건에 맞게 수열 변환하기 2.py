def solution(arr):
    cnt = 0
    while True:
        arr1 = []
        for i in arr:
            if (i >=50) and (i % 2 == 0):
                i = i //2
                arr1.append(i)
            elif ( i < 50) and (i % 2 != 0):
                i = i*2 +1
                arr1.append(i)
            else:
                arr1.append(i)
        if arr1 == arr:
            return cnt
        arr = arr1
        cnt +=1