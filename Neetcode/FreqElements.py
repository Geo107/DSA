from collections import Counter
def FreqElements(nums,k):
    #[1,2,2,3,3,3] , k=2 print top k frequent Elements
    count = Counter(nums)
    lis = []
    for key,val in count.most_common(k):
        lis.append(key)
    return (lis)
