
# write a function that takes a list of integers and returns the largest number in the list
# loop through the list for i in nums
# introduce a variable and set it to 0
# compare i with the variable: if variable>i, then variable. if variable<i, then variable = i.


nums = [3,7,2,9,4]

def find_max(nums):
    n = nums[0]

    for i in nums:
        if n < i:
            n = i
    return n

print(find_max(nums))
