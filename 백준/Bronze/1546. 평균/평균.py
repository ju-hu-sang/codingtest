exam_num = int(input())
score_lst = list(map(int,input().split()))
M = max(score_lst)
new_score = [score/M*100 for score in score_lst]
score_avg = sum(new_score)/exam_num
print(round(score_avg,2))