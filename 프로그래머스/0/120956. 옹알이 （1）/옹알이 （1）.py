def solution(babbling):
    sentence = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for bab in babbling:
        bin = bab
        for doc in sentence:
            bin = bin.replace(doc," ")
        if bin.strip() =="":
            cnt +=1
    return cnt