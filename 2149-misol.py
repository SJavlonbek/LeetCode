def rearrangeArray(nums):
    nums1=[]
    nums2=[]
    nums3=[]
    for i in range(len(nums)):
        if nums[i]>0:
            nums1.append(nums[i])
        else:
            nums2.append(nums[i])

    for n, ns in zip(nums1, nums2):
        nums3.extend([n,ns])
    return nums3

print(rearrangeArray([3,1,-2,-5,2,-4]))

