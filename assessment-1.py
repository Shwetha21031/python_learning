def first_half(input_string):
    length = 0
    for char in input_string:
        length += 1
    midpoint = length // 2
    first_half_str = ''
    for i in range(midpoint):
        first_half_str += input_string[i]

    return first_half_str

def countNums(l,n):
    count = 0
    for i in l:
        if i==n : count+=1
    return count

print(countNums([1,4,9,9,2,9],9))   
    
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

print(diff([1,4,3,9]))


def delAnElem(l,n):
    newl = []
    for i in l:
        if(i!=n):
            newl.append(i)
    return newl

print(delAnElem([2,2,4,5,4,6],2))
        
        
def find_unique_elems(input):
    unique = []

    for elem in input:
        if elem not in unique:
            unique.append(elem)

    return unique

print(find_unique_elems([1,2,3,5,5,4,5,6,3,6]))



def bubble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    
    return
            
original_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(original_list)
print("Sorted list:", original_list)