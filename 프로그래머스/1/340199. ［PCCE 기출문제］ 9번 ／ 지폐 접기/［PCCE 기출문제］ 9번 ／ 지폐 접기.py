def solution(wallet, bill):
    answer = 0
    w = sorted(wallet)
    b = sorted(bill)
    while b[0] > w[0] or b[1] > w[1]:
        if b[1] > b[0]:
            b[1] //= 2
        else:
            b[0] //= 2
        b.sort()
        answer += 1
    return answer