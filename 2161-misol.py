def pivotArray(nums, pivot):
    nums1=[]
    nums2=[]
    nums3=[]
    for i in range(len(nums)):
        if pivot>nums[i]:
            nums1.append(nums[i])
    for j in range(len(nums)):
        if pivot==nums[j]:
            nums2.append(nums[j])
    for x in range(len(nums)):
        if pivot<nums[x]:
            nums3.append(nums[x])
    return nums1+nums2+nums3


print(pivotArray([9,12,5,10,14,3,10],10))