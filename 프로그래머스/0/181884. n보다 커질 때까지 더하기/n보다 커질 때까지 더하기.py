def solution(numbers, n):
    add =[]
    for i in numbers:
        add.append(i)
        if sum(add) > n:
            return sum(add)