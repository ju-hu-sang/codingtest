def solution(a, b, c, d):
    answer = 0
    dice = [a,b,c,d]
    nums = list(set(dice))
    counts = [dice.count(num) for num in nums]
    if len(nums) ==1:
        return nums[0]*1111
    elif len(nums)==2:
        if 3 in counts:
            p = nums[counts.index(3)]
            q = nums[counts.index(1)]
            return (10*p+q)**2
        else:
            p = nums[0]
            q = nums[1]
            return (p+q)*abs(p-q)
    elif len(nums) ==3:
        p = nums[counts.index(2)]
        alone = [num for num in nums if num!=p ]
        return alone[0]*alone[1]
    else:
        return min(dice)
    
