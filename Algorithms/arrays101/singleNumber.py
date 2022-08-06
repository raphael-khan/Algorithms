# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.


nums = [4,1,2,1,2]
# initialize an empty dictionary. 
#  we will need a loop. The loop will be the length of the array.
# add the value to the dictionary.
#  if the value is already in the dictionary, delete it. 
# return the value left in the dict

def singleNumber():
    counts = {}
    for i in nums:
        if i not in counts:
            counts[i] = 1
        else: 
            del counts[i]
    return list(counts.keys())[0]

print(singleNumber())