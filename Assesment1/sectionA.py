# 1 --
def half(s):
    return s[0:int(len(s)/2)]

# print(half("HelloThere"))


# 2 
def revList(l):
    l.reverse()
    return l

# print(revList([1,2,3]))
# print(revList([1,2,3]))


# 3 --
def count9(l,num):
    return l.count(num)

# print(count9([1,9,9,3,9],9))


# 4 --
def countunique(l):
    sum = 0
    for i in l:
        if l.count(i)>1:
            continue
        sum+=i  
    return sum

# print(countunique([3,3,3]))
# print(countunique([2,9,2]))


# 5 --
def diffBetweenNums(l):
    return max(l) - min(l)

# print(diffBetweenNums([10,3,5,6]))
# print(diffBetweenNums([5,1,6,1,9,9]))









