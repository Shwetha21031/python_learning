l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

# 1.1  --
def mergeLists(l1,l2):
    l3 = l1+l2
    return l3
print(mergeLists(l1,l2))


# 1.2 --
def add15(l,index):
    l.insert(index,15)
    return l
# print(add15(l2,-1))


# 1.3 --
def delete4(l):
    l.remove(4)
    return l
# print(delete4(l1))


# 1.4
def addData(l):
    l.append("DATA")
    return l
# print(addData(l1))


# 1.5
def mergeAndRev(l1,l2):
    l1.reverse()
    l2.reverse()
    l3 = l1+l2
    return l3
# print(mergeAndRev(l1,l2))


# 2 --
sampleDict = {
    "Class":{
        "Student":{
            "Name":"Mike",
            "marks":{
                "Physics":70,
                "History":80
            }
        }
    }
}

# print("Marks of history" ,sampleDict["Class"]["Student"]["marks"]["History"])

def findVal(d):
    for i in d.values():
        if type(i) == dict:
            findVal(i)
        else:
                print(i)
print(findVal(sampleDict))


# 3 --
def uniqueElem(l):
    newl = set(l)
    return list(newl)
# print(uniqueElem([1,1,2,1,3,4,4]))


# 4 --
def sortList(l):
    l.sort()
    return l
# print(sortList([3,4,2,5,3]))



# 5
d = {
    1 : "a",
    2 : "b",
    3 : "c"
}
def extractKeys(dict):
    return list(dict.keys())
# print("Keys of dictionary: ",extractKeys(d))












