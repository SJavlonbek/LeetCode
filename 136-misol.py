def singleNumber(nums):
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    singles = [num for num, count in count_dict.items() if count == 1]

    return singles

nums = [1,4,2, 2, 3, 3, 4]
print(singleNumber(nums))
