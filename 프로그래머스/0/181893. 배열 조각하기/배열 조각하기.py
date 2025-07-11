def solution(arr, query):
    
    for idx, i in enumerate(query):
        if idx % 2 ==0:
            arr = arr[:query[idx]+1]
        else:
            arr = arr[query[idx]:]
    return arr
        