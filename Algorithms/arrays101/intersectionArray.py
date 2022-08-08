# Given two integer arrays nums1 and nums2, return an array of their intersection.

from collections import Counter


# nums1 = [1,2,2,1]
# nums2 = [2,2]

# c = (Counter(nums1))
# print(c[3])

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

def intersect():
    c = Counter(nums1) # {4:1 , 9:1, 5:1}
    output = []
    for i in nums2:
        if c[i] > 0:
            output.append(i)
            c[i] -= 1 #decrease counter by 1 so we dont duplicate
    return output

# print(intersect())


def intersectSorted():
    i,j = 0, 0 
    output = []
    nums1, nums2 = sorted(nums1), sorted(nums2)
    print(nums1, nums2)
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            output.append(nums1[i])
            i += 1
            j += 1
    return output
print(intersectSorted())



