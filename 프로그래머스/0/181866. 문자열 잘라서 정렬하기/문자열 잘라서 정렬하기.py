def solution(myString):
    myString = [i for i in myString.split('x') if i]
    m = sorted(myString)
    return m