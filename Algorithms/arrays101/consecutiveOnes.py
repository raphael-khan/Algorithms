# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# You see two sequences of 1's. The first two digits and the last three. You need to return 3 as that is the max number of seq 1
# arr = [1,1,0,1,1,1]

def maxConsecutiveOnes():
    count = 0
    result = 0 
    for i in range(len(arr)):
        if arr[i] == 0:
            count = 0 
        else: 
            count += 1
            result = max(result, count)
    return result

print(maxConsecutiveOnes())

arr = [1,1,0,1,1,1]


def maxConsecutiveOnes():
    maxCount = 0
    count = 0
    for i in arr:
        if i == 1:
            count += 1
            if count > maxCount:
                maxCount = count
        else: 
            count = 0
    return maxCount

print(maxConsecutiveOnes())




