def ProductItself(nums):
    # nums = [1,2,3,4]
    l_mult = 1
    r_mult = 1
    n = len(nums)
    l_arr = [0]*n
    r_arr = [0]*n
    for i in range(n):
        j = -i-1
        l_arr[i]=l_mult
        r_arr[j]=r_mult
        l_mult*=nums[i]
        r_mult*=nums[j]
        #l_arr = all to the left of array muliplied
    return [l*r for l,r in zip(l_arr,r_arr)]
