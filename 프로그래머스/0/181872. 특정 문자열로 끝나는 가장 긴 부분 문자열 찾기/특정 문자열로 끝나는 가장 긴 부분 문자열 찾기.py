def solution(myString, pat):
    index = myString[::-1].find(pat[::-1])
    return myString[:len(myString)-index]