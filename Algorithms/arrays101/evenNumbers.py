# nums = [879, 45]
# print(len(str(nums[0])))

nums = [12,345,2,6,7896]

def findNumbers():
        count = 0 
        for i in range(0,len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count +=1 
            else:
                count = count
        return count

print(findNumbers())

# print(2%2)
# print(3%2)
# print(1%2)
# print(1%2)
# print(4%2)