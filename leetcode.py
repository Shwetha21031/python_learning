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


# 
def factnZeros(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    s = str(fact)[::-1]
    print(s)
    zeros = 0
    for i in s:
        if i == "0":
            zeros+=1
        else:
            break
    print(zeros,"zero's")
    
# factnZeros(10)


# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
def removeElement( nums, val):
    # newNums = filter(lambda i: i!=val , nums)
    # nums = list(newNums) + ([0] * nums.count(val))
    # return nums
    i = 0  
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
# print(removeElement([0,1,2,2,3,0,4,2],2))

# Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

def searchRange(nums: list[int], target):
    first = 0 
    last = 0
    if target not in nums:
        return [-1,-1]
    else:
        first = nums.index(target)
        rev = nums[::-1]
        last = len(rev) - rev.index(target) - 1
    return [first,last]
    
        
# print(searchRange([5,7,7,8,8,10],7))

# roman to integer
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
def romanToInt(num):
    pass
    
# Letter Combinations of a Phone Number
def letter_combinations(digits):
    if not digits:
        return []
    digit_mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    def backtrack(index, path):
        if index == len(digits):
            result.append(''.join(path))
            return
        letters = digit_mapping[digits[index]]
        for letter in letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result

digits = "23"
output = letter_combinations(digits)
# print(output)


# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
def singleNumber(nums):
    for i in nums:
        if (nums.count(i) == 1):
            return i
# print(singleNumber([1,2,1,2,1,2,99]))

# Longest Substring Without Repeating Characters
def lengthOfLongestSubstring( s):
    if(s == "" or s == " "):
        return len(s)
    l = []
    string = ''
    for i in s:
        if (i not in string):
            string+=i
        else:
            l.append(len(string))
            string=i
    l.append(len(string))
    if( len(l) > 1):
        return max(l)
    else:
        return len(l[0])
      
        
        
    
# print(lengthOfLongestSubstring("dvdf"))



# Largest Number
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

# Input: nums = [3,30,34,5,9]
# Output: "9534330"
def largestNumber( nums):
    numbers = []
    
    newnums = list(map(lambda n: str(n),nums))
    newnums.sort(reverse = True)
    string = "".join(newnums)
    return string
    
# print(largestNumber([10,2]))



#  Student Attendance Record I
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
def checkRecord(s):
    if(s.count("A") >= 2):
            return False
    if(len(s)>2):
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] == s[i + 2] == 'L':
                return False
    return True
# print(checkRecord("PPALLL"))

#  Plus One
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
def plusOne(digits):
    strings = ""
    for number in digits:
        strings += str(number)

    temp = str(int(strings) +1)

    return [int(temp[i]) for i in range(len(temp))]
        

# print(plusOne([4,3,2,1]))

# Reverse Words in a String III
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
def reverseWords( s):
    # s = s.split(" ")   
    # l = []
    # for i in s:
    #     l.append(i[::-1])
    # return " ".join(l)
    return " ".join(i[::-1] for i in s.split(" "))

# print(reverseWords("Let's"))

#  Reverse String II
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
def reverseStr( s:str, k:int):
    # return (s[0:k][::-1] + s[k:])
    pass
# print(reverseStr("abcdefg",2))


# missing number
# Input: nums = [0,1]
# Output: 2
def missingNumber( nums):
    m = max(nums)
    for i in range(m+1):
        if i not in nums:
            return i
    return m+1

# print(missingNumber([9,6,4,2,3,5,7,0,1]))    
    
# merge intervals
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
def merge(intervals):
        intervals=sorted(intervals)
        res=[intervals[0]]
        for start,end in intervals[1:]:
            lastEnd=res[-1][1]
            if lastEnd>=start:
                res[-1][1]=max(lastEnd,end)
            else:
                res.append([start,end])
        return res

# print(merge([[1,3],[2,6],[8,10],[15,18]]))


s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
def isPalindrome(s):
    s2 = ""
    for i in s:
        if(i.isalpha()):
            s2 += i.lower()
    s2.split(" ")
    s3 = "".join(s2)
    print(s3)
    print(s3[::-1])
    if(s3[::-1] == s3):
        return True
    return False

    
# print(isPalindrome("A man, a plan, a canal: Panama"))

# longest consecutie sequense
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

def longestConsecutive( nums):
    l = []
    nums.sort()
    m = [nums[0]]
    for i in range(1,len(nums)):
        if ((nums[i] == nums[i-1]) or ( nums[i-1] == (nums[i]-1))):
            m.append(nums[i])
        else:
            l.append(m)
            m.clear()
    return l
        

print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
