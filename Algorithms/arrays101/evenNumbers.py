# nums = [879, 45]
# print(len(str(nums[0])))


nums = [12,345,2,6,7896]

def findNumbers():
        count = 0 
        for i in range(0,len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count +=1 
        return count
# not declarative 
# we are constantly changing the value of count. 
# we only get the value of count once the loop is finsihed. 
# not time and space efficient. 



def findNumbers(self, nums: List[int]) -> int:
    return len([i for i in nums if len(str(i)) % 2 == 0])

# print(findNumbers())

#  To count how many even numbers are in the array. 
nums = [12,345,2,6,7896]

def evenNumbers():
    count = 0 
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1
    return count

print(evenNumbers())