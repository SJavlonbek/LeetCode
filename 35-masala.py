# def searchInsert(nums, target):
#     for i in range(len(nums)):
#         if target==nums[i]:
#             return i
#         elif nums[i]<target:
#             return i+1
# print(searchInsert([1,4,7,9],9))

def searchInsert(nums, target):
    for i in range(len(nums)):
        if target <= nums[i]:
            return i
    return len(nums)

print(searchInsert([1, 4, 7, 9], 4))
