
# given a list of integers, return True if any number appears more than once. Otherwise, return False.
# set n = nums[0]
# create a for loop for i in nums to operate individual element in the list
# if n = nums[i+1], then True, else False

# list to be used
nums = [5,4,1]

# define function with one parameter: nums list
def contain_duplicate(nums):

# created for loop for 0 to 3
    for i in range(len(nums)):
        # for loop for 1 to 3
        for j in range(i+1, len(nums)):
            
            if nums[i] == nums[j]:
                return True
            
    else:
        # then false
        return False
        
# print the function with given parameter
print(contain_duplicate(nums))
