def solution(id_pw, db):
    lgin = 0
    wrong_pw = 0
    fail = 0
    for i,j in db:
        if id_pw[0] == i :
            if id_pw[1] == j:
                return "login"
            else:
                return "wrong pw"
    return "fail"