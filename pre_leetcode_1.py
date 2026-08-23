
# Write a function that takes a list of integers and returns how many number are EnvironmentError
# one element in nums, so i in nums
# variable for counting evens and then +1 if i is even else +0
# i is even if (i%2==0)
# return variable 


nums = [1,2,3,4,6,7]

def count_evens(nums):
    evens = 0
    for i in nums:
        if (i%2==0):
            evens += 1
        else:
            evens += 0
        
    return evens

print(count_evens(nums))
