# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# You see two sequences of 1's. The first two digits and the last three. You need to return 3 as that is the max number of seq 1
arr = [1,1,0,1,1,1]

def maxConsecutiveOnes(arr, n):
    count = 0
    result = 0 
    for i in range(0,n):
        if arr[i] == 0:
            count = 0 
        else: 
            count += 1
            result = max(result, count)
    return result

n = len(arr)
print(maxConsecutiveOnes(arr, n))


