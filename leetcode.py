# You are given three strings s1, s2, and s3. You have to perform the following operation on these three strings as many times as you want.
# In one operation you can choose one of these three strings such that its length is at least 2 and delete the rightmost character of it.
# Return the minimum number of operations you need to perform to make the three strings equal if there is a way to make them equal, otherwise, return -1.

# Input: s1 = "abc", s2 = "abb", s3 = "ab"
# Output: 2
# Explanation: Performing operations on s1 and s2 once will lead to three equal strings.
# It can be shown that there is no way to make them equal with less than two operations.

def findMinimumOperations( s1, s2, s3):
    same = 0
    length = min(len(s1),len(s2),len(s3))
    for i in range(length):
        if((s1[i]==s2[i]) and (s2[i]==s3[i])):
            same+=1
        else:
            break
    if(same==0):
        return -1
    else:
        return ((len(s1)-same)+(len(s2)-same)+(len(s3)-same))
    
        
        
# print(findMinimumOperations('dac','bac','cac'))


# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
def removeElement( nums, val):
    count = 0
    newNums = []
    for i in nums:
        if(i != val):
            newNums.append(i)
            count+=1
    nums = newNums + [0] * (len(nums) - count)
    return nums

    
    
print(removeElement([1,2,3,2,3,1,4,5,1],1))