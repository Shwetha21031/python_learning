# # Python program to create a new dictionary by extracting the keys from a given dictionary.
d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
keys = ['two', 'five']
d2={}
for k in keys:
   d2[k]=d1[k]
# print (d2)

# # Python program to remove keys with same values in a dictionary.
d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
vals = list(d1.values())
dict = {}
uv = [x for x in vals if vals.count(x)==1]
for k,v in d1.items():
    if v in uv:
        dict.update({k:v})
# print(dict)


# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
def removeElement( nums, val):
    elems = [i for i in nums if i != val]
    return elems

# print(removeElement([2,3,4,5,3,5],3))


#  Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
def create_dict(n):
    dict = {}
    for i in range(1,n+1):
        dict.update({i:i*i})
    return dict    

# print(create_dict(6))

# map two lists into a dictionary
def map_Lists(l1,l2):
    if(len(l1)==len(l2)):
        print(len(l1))
        dict={}
        for i in range(0,len(l1)):
            dict.update({str(l1[i]):str(l2[i])})
        return dict
    else:
        return ("Both List must have equal length")
    
l1 = [2,3,4,5,2,5,5]          
l2 = [3,8,4,6,3,5,5]          
# print(map_Lists(l1,l2))

#  Write a Python program to combine two dictionary by adding values for common keys.
dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}
def combine_dicts(d1,d2):
    for key in d2:
        if key in d1:
            d2[key] = d2[key] + d1[key]
    return(dict)
    
# print(combine_dicts(dict1,dict2),"hiii")

#  Write a Python program to combine values in a list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
# def combine_values(dict):
#     d = {}
#     for keys in dict.items:
        
        
# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
def create_dict(s):
    dict = {}
    for x in s:
        dict.update({str(x):s.count(x)})
    return dict

# print(create_dict("hellooo"))


#  Write a Python program to get the top three items in a shop.
sample_dict = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

def top_3(d):
    dict = {}
    val = list(d.values())
    val.sort(reverse=True)
    top = val[:3]
    print(top)
    for k,v in d.items():
        if v in top:
            dict[k]=v
    return dict
    
# print(top_3(sample_dict))


# Write a Python program to count the number of items in a dictionary value that is a list.
dict = {1:1,2:[3,45,6],3:{"a",4,5},4:[3,6,1]}
def count_lists(d):
    count = 0
    vals = list(d.values())
    for i in vals:
        if(type(i) == list):
            count+=1
    return count
 
# print(count_lists(dict))


# Write a Python program to drop empty items from a given dictionary.
dict = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4':"Pink"}
def clean(d):
    dict = {}
    for k,v in d.items():
        if(v):
            dict.update({k:v})
    return dict

# print(clean(dict))
            
# Write a Python program to filter a dictionary based on values.
dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
def greaterThan(d,m):
    newDict = {}
    for key,value in d.items():
        if(value > m):
            newDict.update({key:value})
    return newDict

# print(greaterThan(dict,180))


# Write a Python program to verify that all values in a dictionary are the same.

def value_check(students, n):
    result = all(x >= n for x in students.values())
    return result
    
# print(value_check(dict,120))


#  Write a Python program to remove a specified dictionary from a given list.
dict = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
def remove_dict(d,v):
    l = []
    for i in range(len(d)):
        if(d[i]['id'] != v):
            dict = {}
            dict.update({"id":d[i]['id'],"color":d[i]['color']})
            l.append(dict)         
    return l

def remove_dictionary(colors, r_id):
    colors[:] = [d for d in colors if d.get('id') != r_id]
    return colors
           
# print(remove_dict(dict,"#FF0000"))



#  A Python Dictionary contains List as a value. Write a Python program to update the list values in the said dictionary.
dict = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}

# def add_marks(d,m):
#     dict = {}
#     for i in d.items():
#         print(i)
#         dict.update()
#     return dict
# print(add_marks(dict,2))

# convert to lists
dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
def convert(d):
    l = [list(i) for i in d.items()]
    return l
    
# print(convert(dict))

#  Write a Python program to extract a list of values from a given list of dictionaries.
dict = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
def extract(d,sub):
    l = [i[sub] for i in d]
    return l

# print(extract(dict,'Math'))


    
        