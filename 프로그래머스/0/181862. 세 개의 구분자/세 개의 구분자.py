import re
def solution(myStr):
    myStr1 = re.split('[abc]', myStr)
    answer = []
    for i in myStr1:
        if i:
            answer.append(i)
            
    return answer if answer else ['EMPTY']