def solution(quiz):
    answer = []
    for q in quiz:
        x, op, y, equ, z = q.split()
        x, y, z = int(x), int(y), int(z)
        
        if op == "+":
            result = x + y
        else:
            result = x - y

        answer.append("O" if result == z else "X")
    return answer
