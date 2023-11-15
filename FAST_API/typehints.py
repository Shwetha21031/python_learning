# These "type hints" or annotations are a special syntax that allow declaring the type of a variable.

# without type hints
# def get_full_name(first_name , last_name):
#     full_name = first_name. (if you ctrl+space , no suggestions)

# with type hints
# def get_full_name(first_name :str, last_name:str):
#     full_name = first_name. (now youll get all the suggestions related to string)

# That is not the same as declaring default values like would be with:
#     first_name="john", last_name="doe"
# It's a different thing.

# We are using colons (:), not equals (=).


#  Because the editor knows the types of the variables, you don't only get completion, you also get error checks:

# Now you know that you have to fix it, convert age to a string with str(age):
def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


# Generic types with type parameters¶
# There are some data structures that can contain other values, like dict, list, set and tuple. And the internal values can have their own type too.

# You can use the same builtin types as generics (with square brackets and types inside):
# list
# tuple
# set
# dict
# And the same as with Python 3.8, from the typing module:

# Union
# Optional



# List
# variable to be a list of str.
def process_items(items: list[str]):
    for item in items:
        print(item)

# Tuple and Set
def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

# Dict 
# To define a dict, you pass 2 type parameters, separated by commas.
# The first type parameter is for the keys of the dict.
# The second type parameter is for the values of the dict:
def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

# Union
# You can declare that a variable can be any of several types, for example, an int or a str.
def process_item(item: int | str):
    print(item)

# Possibly None
# You can declare that a value could have a type, like str, but that it could also be None.

from typing import Optional
def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
# Using Optional[str] instead of just str will let the editor help you detecting errors where you could be assuming that a value is always a str, when it could actually be None too.

# Optional[Something] is actually a shortcut for Union[Something, None], they are equivalent.
        
# you can use Something | None:
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

        

# 🚨 Avoid using Optional[SomeType]
# Instead ✨ use Union[SomeType, None] ✨.
        


def say_hi(name: Optional[str]):
    print(f"Hey {name}!")
# The parameter name is defined as Optional[str], but it is not optional, you cannot call the function without the parameter
    
# e good news is, once you are on Python 3.10 you won't have to worry about that, as you will be able to simply use | to define unions of types:

def say_hi(name: str | None):
    print(f"Hey {name}!")



# Classes as types
# You can also declare a class as the type of a variable.
class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


# Pydantic models
# Pydantic is a Python library to perform data validation.
# You declare the "shape" of the data as classes with attributes.
# And each attribute has a type.
# Then you create an instance of that class with some values and it will validate the values, 
# from datetime import datetime

from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
print(user.id)
