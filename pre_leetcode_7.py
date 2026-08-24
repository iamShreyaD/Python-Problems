
# given a list of integers, return the second largest distinct number
# find largest number n
# form list a which consists numbers less than n
# find the largest number in a
# list of integers
nums = [3,7,2,9,4]

# function for second largest integer with parameter of the list
def second_largest(nums):
    n = nums[0]
    for i in nums:
        if i > n:
            n = i

    a = []
    for i in nums:
        if n > i:
            a.append(i)

    m = a[0]
    for i in a:
        if i > m:
            m = i

    return m

print(second_largest(nums))
