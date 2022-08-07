# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

from typing import Counter

s = "loveleetcode"
Output = 0

# build a hash map using Counter. Counter will put value and its count in a hash table. non repeating will have a value of 1. 
# loop through the string.
# compare it with map. put a condition == 1, return that index else -1

def uniqueChar(s):
    hashMap = Counter(s)
    for idx, chr in enumerate(s):
        if hashMap[chr] == 1:
            return idx, chr
    return -1

print(uniqueChar(s))

# Space complexity would be O(1) because amount of unique characters would only be 26
# Time complexity would be O(N) because loop time could increase as the input increases. 