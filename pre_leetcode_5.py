
# write a function that takes a list of integers and returns the smallest number in the list

nums = [7, 3, 9, 2, 5]

def find_min(nums):
    min = nums[0]

    for i in nums: 
        if i < min:
            min = i

    return min

print(find_min(nums))
