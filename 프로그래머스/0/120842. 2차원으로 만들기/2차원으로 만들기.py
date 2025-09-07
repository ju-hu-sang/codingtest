def solution(num_list, n):
    answer = []
    row = len(num_list)//n
    col = n
    for i in range(row):
        answer.append(num_list[n*i:n*(i+1)])
    return answer