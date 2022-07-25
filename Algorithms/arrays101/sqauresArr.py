# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

from numpy import sort


nums = [-4,-1,0,3,10]
# to iterate the array and square value at each index, map func
# sort the result arr in asc order. 

# using sort algorithm - quick sort.
def sortedSquares():
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    nums.sort()
    return nums

print(sortedSquares())
