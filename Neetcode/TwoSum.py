def TwoSum(nums,target):
    count = {}
    for i,c in enumerate(nums):
        diff = target-c
        if diff in count:
            return [count.get(diff),i]
        count[c]=i
    return [0]
