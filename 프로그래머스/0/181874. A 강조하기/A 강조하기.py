def solution(myString):
    new = ""
    for i in myString:
        if i == 'a' or i=='A':
            new += i.upper()
        else:
            new += i.lower()
    return new
        
            