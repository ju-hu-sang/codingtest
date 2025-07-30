def solution(myString):
    new_string = ""
    myString = myString.lower()
    for i in myString:
        if ord(i) < ord('l'):
            i = 'l'
            new_string+=i
        else:
            new_string +=i
    return new_string