def solution(array):
    result = []
    max1 = max(array)
    result.append(max1)
    result.append(array.index(max1))
    return result