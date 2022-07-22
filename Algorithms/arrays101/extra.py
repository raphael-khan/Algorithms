def getMaxLength(arr, n):
 
    # initialize count
    count = 0
     
    # initialize max
    result = 0
 
    for i in range(0, n):
     
        # Reset count when 0 is found
        if (arr[i] == 0):
            count = 0
 
        # If 1 is found, increment count
        # and update result if count
        # becomes more.
        else:
             
            # increase count
            count+= 1
            result = max(result, count)
         
    return result
 
# Driver code
arr = [1, 1, 0, 0, 1, 0, 1,
             0, 1, 1, 1, 1]
n = len(arr)
 
print(getMaxLength(arr, n))
 