def getSumAbsoluteDifferences( nums) :
    nums1=[]
    # s=0
    for i in range(len(nums)):
        s=0
        for j in range(len(nums)):
            s+=abs(nums[i]-nums[j])
        nums1.append(s)
        s=0
    return nums1

print(getSumAbsoluteDifferences([2,3,5])) #[4,3,5]