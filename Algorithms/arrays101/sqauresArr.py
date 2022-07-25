# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

from numpy import sort


nums = [-4,-1,0,3,10]
# to iterate the array and square value at each index, map func
# sort the result arr in asc order. 

# using sort algorithm - quick sort= nlogn
def sortedSquares():
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    nums.sort()
    return nums

# improving the time complex by not using the sort algo. O(n)

def sortedSquares():
    res = []
    l, r = 0, len(nums)-1
    while l <= r:
        if nums[l]**2 > nums[r]**2:
            res.append(nums[l]**2)
            l += 1
        else:
            res.append(nums[r]**2)
            r -= 1
    return res[::-1] #reverse.

print(sortedSquares())
