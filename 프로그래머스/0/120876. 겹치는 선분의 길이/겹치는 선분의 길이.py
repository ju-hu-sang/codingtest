def solution(lines):
    cnt = [0] * 201
    for a, b in lines:
        for x in range(min(a, b), max(a, b)):
            cnt[x + 100] += 1
    return sum(1 for c in cnt if c >= 2)
