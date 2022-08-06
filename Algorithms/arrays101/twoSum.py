# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# nums = [2,7,11,15]

def bruteForceTargetSum(target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]

print(bruteForceTargetSum(9))

nums = [2,11,15,7]

def targetSum(target):
    preMap = {} # val : index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in preMap:
            return [preMap[diff], i ]
        preMap[n] = i 

print(targetSum(9))
