# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.


# to iterate over the array
# if index value == 0 
# then value right to it becomes 0 as well

arr = [ 1,0,2,3,0,4,5,0]
def duplicateZero():
    i = 0
    while i < len(arr):
        if arr[i] == 0:      # finds 0
            arr.insert(i+1,0)  # inserts 0 to the next index.
            del arr[len(arr)-1] # del the last value to keep length the same.
            # arr.pop() could also be used instead of del.
            i += 2   # move the i over twice if 0 is already added. 
        else:
            i += 1   # move the i by 1 if no 0
    return arr
print(duplicateZero())