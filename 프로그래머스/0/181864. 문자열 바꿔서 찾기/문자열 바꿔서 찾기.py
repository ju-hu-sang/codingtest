def solution(myString, pat):
    st = ''
    for i in myString:
        if i == 'A':
            i ='B'
            st +=i
        else:
            i ='A'
            st +=i
    if pat in st :
        return 1
    else:
        return 0 