def solution(num_list):
    answer = []
    
    if num_list[-1] > num_list[-2]:
        answer.append(num_list[-1] - num_list[-2])
        return num_list+answer
    else:
        answer.append(num_list[-1]*2) 
        return num_list+answer
        
    return answer