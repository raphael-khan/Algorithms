# Given an array, rotate the array to the right by k steps, where k is non-negative.

# You have an array. 
# start two pointers and reverse the entire array

nums = [1,2,3,4,5,6,7]

def rotateArray(k):
    k = k % len(nums)  # making sure K is not greater than len of the array
    l , r = 0, len(nums) -1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r -1
    l , r = 0, k -1
    while l < r:
        nums[l], nums[r] = nums[r] , nums[l]
        l , r = l + 1, r -1
    l , r = k , len(nums) -1
    while l < r:
        nums[l] , nums[r] = nums[r] , nums[l]
        l , r = l + 1, r -1
    return nums
print(rotateArray(3))