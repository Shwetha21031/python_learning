import os
def first_half(input_string):
    length = 0
    for char in input_string:
        length += 1
    midpoint = length // 2
    first_half_str = ''
    for i in range(midpoint):
        first_half_str += input_string[i]

    return first_half_str
# print(first_half("HelloWorlddd"))

def countNums(l,n):
    count = 0
    for i in l:
        if i==n : count+=1
    return count
# print(countNums([1,4,9,9,2,9],9))   

def diff(l):
    sm = l[0]
    lg = l[0]
    for elem in l:
        if elem < sm:
            sm = elem
        elif elem > lg:
            lg = elem
    difference = lg - sm
    return difference
# print(diff([1,4,3,9]))


def delAnElem(l,n):
    newl = []
    for i in l:
        if(i!=n):
            newl.append(i)
    return newl
# print(delAnElem([2,2,4,5,4,6],2))
        
        
def find_unique_elems(input):
    unique = []
    for elem in input:
        if elem not in unique:
            unique.append(elem)

    return unique
# print(find_unique_elems([1,2,3,5,5,4,5,6,3,6]))


def bubble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    
    return
# original_list = [4,5,6,2,9,4,9]
# bubble_sort(original_list)
# print("Sorted list: ", original_list)


def add15(l,index):
    newl = []
    if ((index == -1) or (index >= len(l))):
        l.append(15)
        return l
    for i in range(len(l)):
        print(i)
        if (i != index):
            newl.append(l[i])
        else:
            newl.append(15)
            newl.append(l[i])
    return newl
    
# print(add15([1,2,5,3,6],7))           


l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

def mergeList(l1,l2):
    newl = []
    for i in l1:
        newl.append(i)
    for i in l2:
        newl.append(i)
    return newl

# print(mergeList(l1,l2)[-1])


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


def find_by_key(data, target):
    for k, v in data.items():
        if k == target:
            return v
        elif isinstance(v, dict):
            return find_by_key(v, target)
        
    return "key not found"

# print(find_by_key(sampleDict,"History"))

# making multiple folders at once
# root_folder = "Archive-viewer"
# sub_folders = ["Front_end","Back_end","QA"]
# try :
#     for i in sub_folders:
#         os.makedirs(f'{root_folder}/{i}')
# except:
#     print("folders already created")
