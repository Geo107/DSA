def ContainingWater(nums):
    # nums are boundary that allows water to be filled
    l,r = 0,len(nums)-1
    max_area = 0
    while l<r:
        height = min(nums[l],nums[r])
        area = height * (r-l)
        if nums[l]<nums[r]:
            l+=1
        else:
            r-=1
        max_area =max(max_area,area)
    return max_area
