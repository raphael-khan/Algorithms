# Write a function that reverses a string. The input string is given as an array of characters.

# Input = ["h","e","l","l","o"]
# Output = ["o","l","l","e","h"]

# two pointer technique. 
# start on left, one on the right. top in the middle. 

array = ["h","e","l","l","o"]

def reverseArray(arr):
    l ,r = 0 , len(arr)-1
    while l < r: #while they have not met or crossed.
        arr[l] , arr[r] = arr[r] , arr[l]
        l , r = l + 1 , r - 1
    return arr


print(reverseArray(array))
# space complexity O(1) => constant space as the input increases algo modifies string in place. 
# time complexity O(N) => as input size increases time will increase proportionality. 