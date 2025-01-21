while True:
    n = int(input())
    if n == -1 :
        break
    n_list = []
    for i in range(1,n+1):
        if n%i ==0:
            n_list.append(i)
    new_n_list = n_list.pop()
        
    if sum(n_list) == new_n_list:
        n_list_str = ' + '.join(map(str,n_list))
        print(f"{n} = {n_list_str}")
    else:
        print(f"{n} is NOT perfect.")