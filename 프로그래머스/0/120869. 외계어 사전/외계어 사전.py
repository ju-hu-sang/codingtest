def solution(spell, dic):
    cnt = 0
    for i in dic:
        if len(set(spell) & set(i)) == len(spell):
            cnt +=1
        else:
            continue
    return 1 if cnt >0 else 2
