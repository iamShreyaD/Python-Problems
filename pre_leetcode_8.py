

# given a list of integers, move all 0s to the end of the list 
# while keeping the relative order of the non-zero elements.

nums = [0,1,0,3,12]
def move_zeroes(nums):
    num = 0
    count = 0

    # for loop to count and remove zeroes
    # for i in range(4, -1, -1)
    for i in range(len(nums) - 1, - 1, - 1):
        # if the number is 0
        if nums[i] == num:
            count += 1
            nums.pop(i) 
    
    # now the list is [1,3,12] with count = 2
    # for loop to add zeroes at the end
    for i in range(count):
        nums.append(0)
    return nums 
    
print(move_zeroes(nums))
        
