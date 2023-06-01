def find_duplicate(nums):
    nums.sort()
    for index in range(len(nums) - 1):
        curr_num = nums[index]
        if not isinstance(curr_num, int) or curr_num < 1:
            return False
        next_num = nums[index + 1]
        if curr_num == next_num:
            return nums[index]
    else:
        return False


print(find_duplicate([1, 2]))
