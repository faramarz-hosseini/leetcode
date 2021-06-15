def running_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return_list = [nums[0]]
    for i in nums[1:]:
        return_list.append(return_list[-1] + i)

    return return_list


print(running_sum([1,2,3,4]))
