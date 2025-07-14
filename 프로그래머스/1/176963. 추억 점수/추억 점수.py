def solution(name, yearning, photo):
    answer = []
    new_dict = dict(zip(name, yearning))
    for i in photo:
        cnt = 0
        for j in i:
            cnt += new_dict.get(j, 0)
        answer.append(cnt)
    return answer