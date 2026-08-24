

# given a list of integers, move all 0s to the end of the list 
# while keeping the relative order of the non-zero elements.

nums = [0,1,0,3,12]

def move_zeroes(nums):
    a = 0
    count = 0

    for i in nums:
        # if i is 0
        if i == a:
            # increase count
            count += 1
            # remove 0 from the list
            nums.remove(i)
            nums.append(a*count)
    return nums

print(move_zeroes(nums))
