def solution(num, total):
    a =  (total - (num*(num-1))//2)//num
    return [a + i for i in range(num)]