def solution(keyinput, board):
    x=y=0
    ga = board[0]//2
    se = board[1]//2
    dic = {
        'up':[0,1],
        'down':[0,-1],
        'right':[1,0],
        'left':[-1,0]
    }
    for i in keyinput:
        dx , dy = dic[i]
        if abs(x+dx) <=ga and abs(y+dy) <=se:
            x,y = x+dx, y+dy
    return [x,y]