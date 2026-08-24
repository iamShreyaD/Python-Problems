# write a function that takes a list of integers and returns the sum of only the positive numbers
# set s = 0
# create a loop for i in nums
# varify if the number is positive, if yes s+=i
# return s
# print function

nums = [-2, 3, -1, 5, 0, 4]

def sum_positive(nums):
    s = 0

    for i in nums:
        if i > 0:
            s += i
    return s

print(sum_positive(nums))
