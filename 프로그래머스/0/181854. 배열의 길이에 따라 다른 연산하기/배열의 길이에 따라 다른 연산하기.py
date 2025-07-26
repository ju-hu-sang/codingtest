def solution(arr, n):
    arr1 = []
    arr2 = []
    if len(arr) % 2 ==1 :
        for i in range(len(arr)):
            if i%2 ==0:
                arr1.append(arr[i]+n)
            else:
                arr1.append(arr[i])
        return arr1
    else:
        for i in range(len(arr)):
            if i%2 == 1:
                arr2.append(arr[i]+n)
            else:
                arr2.append(arr[i])
        return arr2