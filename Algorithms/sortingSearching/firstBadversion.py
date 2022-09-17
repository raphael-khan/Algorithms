# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

n = 5, 
bad = 4
Output= 4
[1,2,3,4,5]
def firstBadverison(n):
        #call API every single time.
        #result of API is true
        #return that value of n. 
# if bad version is 4 then we definitely do not want to check after 4. algorithms. 
    start = 1
    end = n
    while start < n: 
        mid = (start + end) // 2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid + 1
    return start
