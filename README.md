Python Cheatsheet
=================

Contents
--------
**&nbsp;&nbsp;&nbsp;** **1. Collections:** **&nbsp;** **[`List`](#list)**__,__ **[`Dictionary`](#dictionary)**__,__ **[`Set`](#set)**__,__ **[`Tuple`](#tuple)**__,__ **[`Range`](#range)**__,__ **[`Enumerate`](#enumerate)**__,__ **[`Iterator`](#iterator)**__,__ **[`Generator`](#generator)**__.__  
**&nbsp;&nbsp;&nbsp;** **2. Types:** **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**  **[`Type`](#type)**__,__ **[`String`](#string)**__,__ **[`Regular_Exp`](#regex)**__,__   **[`Datetime`](#datetime)**__.__  
**&nbsp;&nbsp;&nbsp;** **3. Syntax:** **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**  **[`Args`](#arguments)**__,__  **[`Import`](#imports)**__,__ **[`Decorator`](#decorator)**__,__ **[`Class`](#class)**__,__ **[`Duck_Types`](#duck-types)**__,__ **[`Enum`](#enum)**__,__ **[`Exception`](#exceptions)**__.__  
**&nbsp;&nbsp;&nbsp;** **4. System:** **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**  **[`Exit`](#exit)**__,__ **[`Print`](#print)**__,__ **[`Input`](#input)**__,__  **[`Open`](#open)**__,__ **[`OS_Commands`](#os-commands)**__.__  
**&nbsp;&nbsp;&nbsp;** **5. Data:** **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**  **[`JSON`](#json)**__,__  **[`CSV`](#csv)**__,__ 


Main
----
```python
if __name__ == '__main__':      # Runs main() if file wasn't imported.
    main()
```


List
----
```python
<list> = <list>[<slice>]        # Or: <list>[from_inclusive : to_exclusive : ±step]
```

```python
<list>.append(<el>)             # Or: <list> += [<el>]
<list>.extend(<collection>)     # Or: <list> += <collection>
```

```python
<list>.sort()                   # Sorts in ascending order.
<list>.reverse()                # Reverses the list in-place.
<list> = sorted(<collection>)   # Returns a new sorted list.
<iter> = reversed(<list>)       # Returns reversed iterator.
```

```python
sum_of_elements  = sum(<collection>)
elementwise_sum  = [sum(pair) for pair in zip(list_a, list_b)]
sorted_by_second = sorted(<collection>, key=lambda el: el[1])
sorted_by_both   = sorted(<collection>, key=lambda el: (el[1], el[0]))
flatter_list     = list(itertools.chain.from_iterable(<list>))
product_of_elems = functools.reduce(lambda out, el: out * el, <collection>)
list_of_chars    = list(<str>)
```
* **For details about sorted(), min() and max() see [sortable](#sortable).**
* **Module [operator](#operator) provides functions itemgetter() and mul() that offer the same functionality as [lambda](#lambda) expressions above.**

```python
<list>.insert(<int>, <el>)      # Inserts item at index and moves the rest to the right.
<el>  = <list>.pop([<int>])     # Removes and returns item at index or from the end.
<int> = <list>.count(<el>)      # Returns number of occurrences. Also works on strings.
<int> = <list>.index(<el>)      # Returns index of the first occurrence or raises ValueError.
<list>.remove(<el>)             # Removes first occurrence of the item or raises ValueError.
<list>.clear()                  # Removes all items. Also works on dictionary and set.
```


Dictionary
----------
```python
<view> = <dict>.keys()                          # Coll. of keys that reflects changes.
<view> = <dict>.values()                        # Coll. of values that reflects changes.
<view> = <dict>.items()                         # Coll. of key-value tuples that reflects chgs.
```

```python
value  = <dict>.get(key, default=None)          # Returns default if key is missing.
value  = <dict>.setdefault(key, default=None)   # Returns and writes default if key is missing.
<dict> = collections.defaultdict(<type>)        # Returns a dict with default value `<type>()`.
<dict> = collections.defaultdict(lambda: 1)     # Returns a dict with default value 1.
```

```python
<dict> = dict(<collection>)                     # Creates a dict from coll. of key-value pairs.
<dict> = dict(zip(keys, values))                # Creates a dict from two collections.
<dict> = dict.fromkeys(keys [, value])          # Creates a dict from collection of keys.
```

```python
<dict>.update(<dict>)                           # Adds items. Replaces ones with matching keys.
value = <dict>.pop(key)                         # Removes item or raises KeyError if missing.
{k for k, v in <dict>.items() if v == value}    # Returns set of keys that point to the value.
{k: v for k, v in <dict>.items() if k in keys}  # Returns a dictionary, filtered by keys.
```

### Counter
```python
>>> from collections import Counter
>>> colors = ['blue', 'blue', 'blue', 'red', 'red']
>>> counter = Counter(colors)
>>> counter['yellow'] += 1
Counter({'blue': 3, 'red': 2, 'yellow': 1})
>>> counter.most_common()[0]
('blue', 3)
```


Set
---
```python
<set> = set()                                   # `{}` returns a dictionary.
```

```python
<set>.add(<el>)                                 # Or: <set> |= {<el>}
<set>.update(<collection> [, ...])              # Or: <set> |= <set>
```

```python
<set>  = <set>.union(<coll.>)                   # Or: <set> | <set>
<set>  = <set>.intersection(<coll.>)            # Or: <set> & <set>
<set>  = <set>.difference(<coll.>)              # Or: <set> - <set>
<set>  = <set>.symmetric_difference(<coll.>)    # Or: <set> ^ <set>
<bool> = <set>.issubset(<coll.>)                # Or: <set> <= <set>
<bool> = <set>.issuperset(<coll.>)              # Or: <set> >= <set>
```

```python
<el> = <set>.pop()                              # Raises KeyError if empty.
<set>.remove(<el>)                              # Raises KeyError if missing.
<set>.discard(<el>)                             # Doesn't raise an error.
```

### Frozen Set
* **Is immutable and hashable.**
* **That means it can be used as a key in a dictionary or as an element in a set.**
```python
<frozenset> = frozenset(<collection>)
```


Tuple
-----
**Tuple is an immutable and hashable list.**
```python
<tuple> = ()                               # Empty tuple.
<tuple> = (<el>,)                          # Or: <el>,
<tuple> = (<el_1>, <el_2> [, ...])         # Or: <el_1>, <el_2> [, ...]
```

### Named Tuple
**Tuple's subclass with named elements.**

```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point', 'x y')
>>> p = Point(1, y=2)
Point(x=1, y=2)
>>> p[0]
1
>>> p.x
1
>>> getattr(p, 'y')
2
```


Range
-----
**Immutable and hashable sequence of integers.**
```python
<range> = range(stop)                      # range(to_exclusive)
<range> = range(start, stop)               # range(from_inclusive, to_exclusive)
<range> = range(start, stop, ±step)        # range(from_inclusive, to_exclusive, ±step_size)
```

```python
>>> [i for i in range(3)]
[0, 1, 2]
```


Enumerate
---------
```python
for i, el in enumerate(<collection> [, i_start]):
    ...
```


Iterator
--------
```python
<iter> = iter(<collection>)                # `iter(<iter>)` returns unmodified iterator.
<iter> = iter(<function>, to_exclusive)    # A sequence of return values until 'to_exclusive'.
<el>   = next(<iter> [, default])          # Raises StopIteration or returns 'default' on end.
<list> = list(<iter>)                      # Returns a list of iterator's remaining elements.
```

### Itertools
```python
import itertools as it
```

```python
<iter> = it.count(start=0, step=1)         # Returns updated value endlessly. Accepts floats.
<iter> = it.repeat(<el> [, times])         # Returns element endlessly or 'times' times.
<iter> = it.cycle(<collection>)            # Repeats the sequence endlessly.
```

```python
<iter> = it.chain(<coll>, <coll> [, ...])  # Empties collections in order (figuratively).
<iter> = it.chain.from_iterable(<coll>)    # Empties collections inside a collection in order.
```

```python
<iter> = it.islice(<coll>, to_exclusive)   # Only returns first 'to_exclusive' elements.
<iter> = it.islice(<coll>, from_inc, …)    # `to_exclusive, +step_size`. Indices can be None.
```


Generator
---------
* **Any function that contains a yield statement returns a generator.**
* **Generators and iterators are interchangeable.**

```python
def count(start, step):
    while True:
        yield start
        start += step
```

```python
>>> counter = count(10, 2)
>>> next(counter), next(counter), next(counter)
(10, 12, 14)
```


Type
----
* **Everything is an object.**
* **Every object has a type.**
* **Type and class are synonymous.**

```python
<type> = type(<el>)                          # Or: <el>.__class__
<bool> = isinstance(<el>, <type>)            # Or: issubclass(type(<el>), <type>)
```

```python
>>> type('a'), 'a'.__class__, str
(<class 'str'>, <class 'str'>, <class 'str'>)
```

#### Some types do not have built-in names, so they must be imported:
```python
from types import FunctionType, MethodType, LambdaType, GeneratorType, ModuleType
```

### Abstract Base Classes
**Each abstract base class specifies a set of virtual subclasses. These classes are then recognized by isinstance() and issubclass() as subclasses of the ABC, although they are really not. ABC can also manually decide whether or not a specific class is its virtual subclass, usually based on which methods the class has implemented. For instance, Iterable ABC looks for method iter(), while Collection ABC looks for iter(), contains() and len().**

```python
>>> from collections.abc import Iterable, Collection, Sequence
>>> isinstance([1, 2, 3], Iterable)
True
```

```text
+------------------+------------+------------+------------+
|                  |  Iterable  | Collection |  Sequence  |
+------------------+------------+------------+------------+
| list, range, str |    yes     |    yes     |    yes     |
| dict, set        |    yes     |    yes     |            |
| iter             |    yes     |            |            |
+------------------+------------+------------+------------+
```

String
------
**Immutable sequence of characters.**

```python
<str>  = <str>.strip()                       # Strips all whitespace characters from both ends.
<str>  = <str>.strip('<chars>')              # Strips passed characters. Also lstrip/rstrip().
```

```python
<list> = <str>.split()                       # Splits on one or more whitespace characters.
<list> = <str>.split(sep=None, maxsplit=-1)  # Splits on 'sep' str at most 'maxsplit' times.
<list> = <str>.splitlines(keepends=False)    # On [\n\r\f\v\x1c-\x1e\x85\u2028\u2029] and \r\n.
<str>  = <str>.join(<coll_of_strings>)       # Joins elements using string as a separator.
```

```python
<bool> = <sub_str> in <str>                  # Checks if string contains the substring.
<bool> = <str>.startswith(<sub_str>)         # Pass tuple of strings for multiple options.
<bool> = <str>.endswith(<sub_str>)           # Pass tuple of strings for multiple options.
<int>  = <str>.find(<sub_str>)               # Returns start index of the first match or -1.
<int>  = <str>.index(<sub_str>)              # Same, but raises ValueError if missing.
```

```python
<str>  = <str>.lower()                       # Changes the case. Also upper/capitalize/title().
<str>  = <str>.replace(old, new [, count])   # Replaces 'old' with 'new' at most 'count' times.
<str>  = <str>.translate(<table>)            # Use `str.maketrans(<dict>)` to generate table.
```

```python
<str>  = chr(<int>)                          # Converts int to Unicode character.
<int>  = ord(<str>)                          # Converts Unicode character to int.
```
* **Use `'unicodedata.normalize("NFC", <str>)'` on strings that may contain characters like `'Ö'` before comparing them, because they can be stored as one or two characters.**

### Property Methods
```python
<bool> = <str>.isdecimal()                   # Checks for [0-9].
<bool> = <str>.isdigit()                     # Checks for [²³¹] and isdecimal().
<bool> = <str>.isnumeric()                   # Checks for [¼½¾] and isdigit().
<bool> = <str>.isalnum()                     # Checks for [a-zA-Z] and isnumeric().
<bool> = <str>.isprintable()                 # Checks for [ !#$%…] and isalnum().
<bool> = <str>.isspace()                     # Checks for [ \t\n\r\f\v\x1c-\x1f\x85\xa0…].
```


Regex
-----
**Functions for regular expression matching.**

```python
import re
```

```python
<str>   = re.sub(<regex>, new, text, count=0)  # Substitutes all occurrences with 'new'.
<list>  = re.findall(<regex>, text)            # Returns all occurrences as strings.
<list>  = re.split(<regex>, text, maxsplit=0)  # Add brackets around regex to include matches.
<Match> = re.search(<regex>, text)             # First occurrence of the pattern or None.
<Match> = re.match(<regex>, text)              # Searches only at the beginning of the text.
<iter>  = re.finditer(<regex>, text)           # Returns all occurrences as Match objects.
```

* **Argument 'new' can be a function that accepts a Match object and returns a string.**
* **Argument `'flags=re.IGNORECASE'` can be used with all functions.**
* **Argument `'flags=re.MULTILINE'` makes `'^'` and `'$'` match the start/end of each line.**
* **Argument `'flags=re.DOTALL'` makes `'.'` also accept the `'\n'`.**
* **Use `r'\1'` or `'\\1'` for backreference (`'\1'` returns a character with octal code 1).**
* **Add `'?'` after `'*'` and `'+'` to make them non-greedy.**

### Match Object
```python
<str>   = <Match>.group()                      # Returns the whole match. Also group(0).
<str>   = <Match>.group(1)                     # Returns the part inside first brackets.
<tuple> = <Match>.groups()                     # Returns all bracketed parts.
<int>   = <Match>.start()                      # Returns start index of the match.
<int>   = <Match>.end()                        # Returns exclusive end index of the match.
```

### Special Sequences
```python
'\d' == '[0-9]'                                # Matches decimal characters.
'\w' == '[a-zA-Z0-9_]'                         # Matches alphanumerics and underscore.
'\s' == '[ \t\n\r\f\v]'                        # Matches whitespaces.
```

* **By default, decimal characters, alphanumerics and whitespaces from all alphabets are matched unless `'flags=re.ASCII'` argument is used.**
* **As shown above, it restricts all special sequence matches to the first 128 characters and prevents `'\s'` from accepting `'[\x1c-\x1f]'` (the so-called separator characters).**
* **Use a capital letter for negation (all non-ASCII characters will be matched when used in combination with ASCII flag).**


Numbers
-------
```python
<int>      = int(<float/str/bool>)                # Or: math.floor(<float>)
<float>    = float(<int/str/bool>)                # Or: <int/float>e±<int>
<complex>  = complex(real=0, imag=0)              # Or: <int/float> ± <int/float>j
<Fraction> = fractions.Fraction(0, 1)             # Or: Fraction(numerator=0, denominator=1)
<Decimal>  = decimal.Decimal(<str/int>)           # Or: Decimal((sign, digits, exponent))
```
* **`'int(<str>)'` and `'float(<str>)'` raise ValueError on malformed strings.**
* **Decimal numbers are stored exactly, unlike most floats where `'1.1 + 2.2 != 3.3'`.**
* **Floats can be compared with: `'math.isclose(<float>, <float>)'`.**
* **Precision of decimal operations is set with: `'decimal.getcontext().prec = <int>'`.**

### Basic Functions
```python
<num> = pow(<num>, <num>)                         # Or: <num> ** <num>
<num> = abs(<num>)                                # <float> = abs(<complex>)
<num> = round(<num> [, ±ndigits])                 # `round(126, -1) == 130`
```

### Math
```python
from math import e, pi, inf, nan, isinf, isnan    # `<el> == nan` is always False.
from math import sin, cos, tan, asin, acos, atan  # Also: degrees, radians.
from math import log, log10, log2                 # Log can accept base as second arg.
```

### Statistics
```python
from statistics import mean, median, variance     # Also: stdev, quantiles, groupby.
```

### Random
```python
from random import random, randint, choice        # Also: shuffle, gauss, triangular, seed.
<float> = random()                                # A float inside [0, 1).
<int>   = randint(from_inc, to_inc)               # An int inside [from_inc, to_inc].
<el>    = choice(<sequence>)                      # Keeps the sequence intact.
```

### Bin, Hex
```python
<int> = ±0b<bin>                                  # Or: ±0x<hex>
<int> = int('±<bin>', 2)                          # Or: int('±<hex>', 16)
<int> = int('±0b<bin>', 0)                        # Or: int('±0x<hex>', 0)
<str> = bin(<int>)                                # Returns '[-]0b<bin>'.
```

### Bitwise Operators
```python
<int> = <int> & <int>                             # And (0b1100 & 0b1010 == 0b1000).
<int> = <int> | <int>                             # Or  (0b1100 | 0b1010 == 0b1110).
<int> = <int> ^ <int>                             # Xor (0b1100 ^ 0b1010 == 0b0110).
<int> = <int> << n_bits                           # Left shift. Use >> for right.
<int> = ~<int>                                    # Not. Also -<int> - 1.
```



Datetime
--------
**Provides 'date', 'time', 'datetime' and 'timedelta' classes. All are immutable and hashable.**

```python
# pip3 install python-dateutil
from datetime import date, time, datetime, timedelta, timezone
from dateutil.tz import tzlocal, gettz
```

```python
<D>  = date(year, month, day)               # Only accepts valid dates from 1 to 9999 AD.
<T>  = time(hour=0, minute=0, second=0)     # Also: `microsecond=0, tzinfo=None, fold=0`.
<DT> = datetime(year, month, day, hour=0)   # Also: `minute=0, second=0, microsecond=0, …`.
<TD> = timedelta(weeks=0, days=0, hours=0)  # Also: `minutes=0, seconds=0, microseconds=0`.
```
* **Aware `<a>` time and datetime objects have defined timezone, while naive `<n>` don't. If object is naive, it is presumed to be in the system's timezone!**
* **`'fold=1'` means the second pass in case of time jumping back for one hour.**
* **Timedelta normalizes arguments to ±days, seconds (< 86 400) and microseconds (< 1M).**
* **Use `'<D/DT>.weekday()'` to get the day of the week as an int, with Monday being 0.**


### Arithmetics
```python
<bool>   = <D/T/DTn> > <D/T/DTn>            # Ignores time jumps (fold attribute). Also ==.
<bool>   = <DTa>     > <DTa>                # Ignores time jumps if they share tzinfo object.
<TD>     = <D/DTn>   - <D/DTn>              # Ignores jumps. Convert to UTC for actual delta.
<TD>     = <DTa>     - <DTa>                # Ignores time jumps if they share tzinfo object.
<D/DT>   = <D/DT>    ± <TD>                 # Returned datetime can fall into missing hour.
<TD>     = <TD>      * <float>              # Also: <TD> = abs(<TD>) and <TD> = <TD> ±% <TD>.
<float>  = <TD>      / <TD>                 # How many weeks/years there are in TD. Also //.
```


Arguments
---------
### Inside Function Call
```python
func(<positional_args>)                           # func(0, 0)
func(<keyword_args>)                              # func(x=0, y=0)
func(<positional_args>, <keyword_args>)           # func(0, y=0)
```

### Inside Function Definition
```python
def func(<nondefault_args>): ...                  # def func(x, y): ...
def func(<default_args>): ...                     # def func(x=0, y=0): ...
def func(<nondefault_args>, <default_args>): ...  # def func(x, y=0): ...
```
* **Default values are evaluated when function is first encountered in the scope.**
* **Any mutation of a mutable default value will persist between invocations!**


Splat Operator
--------------
### Inside Function Call
**Splat expands a collection into positional arguments, while splatty-splat expands a dictionary into keyword arguments.**
```python
args   = (1, 2)
kwargs = {'x': 3, 'y': 4, 'z': 5}
func(*args, **kwargs)
```

#### Is the same as:
```python
func(1, 2, x=3, y=4, z=5)
```

### Inside Function Definition
**Splat combines zero or more positional arguments into a tuple, while splatty-splat combines zero or more keyword arguments into a dictionary.**
```python
def add(*a):
    return sum(a)
```

```python
>>> add(1, 2, 3)
6
```

#### Legal argument combinations:
```python
def f(*args): ...               # f(1, 2, 3)
def f(x, *args): ...            # f(1, 2, 3)
def f(*args, z): ...            # f(1, 2, z=3)
```

```python
def f(**kwargs): ...            # f(x=1, y=2, z=3)
def f(x, **kwargs): ...         # f(x=1, y=2, z=3) | f(1, y=2, z=3)
```

```python
def f(*args, **kwargs): ...     # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3) | f(1, 2, 3)
def f(x, *args, **kwargs): ...  # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3) | f(1, 2, 3)
def f(*args, y, **kwargs): ...  # f(x=1, y=2, z=3) | f(1, y=2, z=3)
```

```python
def f(*, x, y, z): ...          # f(x=1, y=2, z=3)
def f(x, *, y, z): ...          # f(x=1, y=2, z=3) | f(1, y=2, z=3)
def f(x, y, *, z): ...          # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3)
```

### Other Uses
```python
<list>  = [*<coll.> [, ...]]    # Or: list(<collection>) [+ ...]
<tuple> = (*<coll.>, [...])     # Or: tuple(<collection>) [+ ...]
<set>   = {*<coll.> [, ...]}    # Or: set(<collection>) [| ...]
<dict>  = {**<dict> [, ...]}    # Or: dict(**<dict> [, ...])
```

```python
head, *body, tail = <coll.>     # Head or tail can be omitted.
```


Inline
------
### Lambda
```python
<func> = lambda: <return_value>                     # A single statement function.
<func> = lambda <arg_1>, <arg_2>: <return_value>    # Also accepts default arguments.
```

### Comprehensions
```python
<list> = [i+1 for i in range(10)]                   # Or: [1, 2, ..., 10]
<iter> = (i for i in range(10) if i > 5)            # Or: iter([6, 7, 8, 9])
<set>  = {i+5 for i in range(10)}                   # Or: {5, 6, ..., 14}
<dict> = {i: i*2 for i in range(10)}                # Or: {0: 0, 1: 2, ..., 9: 18}
```

```python
>>> [l+r for l in 'abc' for r in 'abc']
['aa', 'ab', 'ac', ..., 'cc']
```

### Map, Filter, Reduce
```python
from functools import reduce
```

```python
<iter> = map(lambda x: x + 1, range(10))            # Or: iter([1, 2, ..., 10])
<iter> = filter(lambda x: x > 5, range(10))         # Or: iter([6, 7, 8, 9])
<obj>  = reduce(lambda out, x: out + x, range(10))  # Or: 45
```

### Any, All
```python
<bool> = any(<collection>)                          # Is `bool(<el>)` True for any element.
<bool> = all(<collection>)                          # Is True for all elements or empty.
```

### Conditional Expression
```python
<obj> = <exp> if <condition> else <exp>             # Only one expression gets evaluated.
```

```python
>>> [a if a else 'zero' for a in (0, 1, 2, 3)]      # `any([0, '', [], None]) == False`
['zero', 1, 2, 3]
```

### Named Tuple, Enum, Dataclass
```python
from collections import namedtuple
Point = namedtuple('Point', 'x y')                  # Creates a tuple's subclass.
point = Point(0, 0)                                 # Returns its instance.
```

```python
from enum import Enum
Direction = Enum('Direction', 'N E S W')            # Creates an enum.
direction = Direction.N                             # Returns its member.
```

```python
from dataclasses import make_dataclass
Player = make_dataclass('Player', ['loc', 'dir'])   # Creates a class.
player = Player(point, direction)                   # Returns its instance.
```


Imports
-------
```python
import <module>            # Imports a built-in or '<module>.py'.
import <package>           # Imports a built-in or '<package>/__init__.py'.
import <package>.<module>  # Imports a built-in or '<package>/<module>.py'.
```
* **Package is a collection of modules, but it can also define its own objects.**
* **On a filesystem this corresponds to a directory of Python files with an optional init script.**
* **Running `'import <package>'` does not automatically provide access to the package's modules unless they are explicitly imported in its init script.**


Closure
-------
**We have/get a closure in Python when:**
* **A nested function references a value of its enclosing function and then**
* **the enclosing function returns the nested function.**

```python
def get_multiplier(a):
    def out(b):
        return a * b
    return out
```

```python
>>> multiply_by_3 = get_multiplier(3)
>>> multiply_by_3(10)
30
```

* **If multiple nested functions within enclosing function reference the same value, that value gets shared.**
* **To dynamically access function's first free variable use `'<function>.__closure__[0].cell_contents'`.**

Decorator
---------
* **A decorator takes a function, adds some functionality and returns it.**
* **It can be any [callable](#callable), but is usually implemented as a function that returns a [closure](#closure).**

```python
@decorator_name
def function_that_gets_passed_to_decorator():
    ...
```

### Debugger Example
**Decorator that prints function's name every time the function is called.**

```python
from functools import wraps

def debug(func):
    @wraps(func)
    def out(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return out

@debug
def add(x, y):
    return x + y
```
* **Wraps is a helper decorator that copies the metadata of the passed function (func) to the function it is wrapping (out).**
* **Without it `'add.__name__'` would return `'out'`.**

### LRU Cache
**Decorator that caches function's return values. All function's arguments must be hashable.**

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)
```
* **Default size of the cache is 128 values. Passing `'maxsize=None'` makes it unbounded.**
* **CPython interpreter limits recursion depth to 1000 by default. To increase it use `'sys.setrecursionlimit(<depth>)'`.**

### Parametrized Decorator
**A decorator that accepts arguments and returns a normal decorator that accepts a function.**
```python
from functools import wraps

def debug(print_result=False):
    def decorator(func):
        @wraps(func)
        def out(*args, **kwargs):
            result = func(*args, **kwargs)
            print(func.__name__, result if print_result else '')
            return result
        return out
    return decorator

@debug(print_result=True)
def add(x, y):
    return x + y
```
* **Using only `'@debug'` to decorate the add() function would not work here, because debug would then receive the add() function as a 'print_result' argument. Decorators can however manually check if the argument they received is a function and act accordingly.**


Class
-----
```python
class <name>:
    def __init__(self, a):
        self.a = a
    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.a!r})'
    def __str__(self):
        return str(self.a)

    @classmethod
    def get_class_name(cls):
        return cls.__name__
```
* **Return value of repr() should be unambiguous and of str() readable.**
* **If only repr() is defined, it will also be used for str().**
* **Methods decorated with `'@staticmethod'` do not receive 'self' nor 'cls' as their first arg.**


#### Expressions that call the repr() method:
```python
print/str/repr([<el>])
print/str/repr({<el>: <el>})
f'{<el>!r}'
Z = dataclasses.make_dataclass('Z', ['a']); print/str/repr(Z(<el>))
>>> <el>
```

### Constructor Overloading
```python
class <name>:
    def __init__(self, a=None):
        self.a = a
```

### Inheritance
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

class Employee(Person):
    def __init__(self, name, age, staff_num):
        super().__init__(name, age)
        self.staff_num = staff_num
```

### Multiple Inheritance
```python
class A: pass
class B: pass
class C(A, B): pass
```


### Dataclass
**Decorator that automatically generates init(), repr() and eq() special methods.**
```python
from dataclasses import dataclass, field

@dataclass(order=False, frozen=False)
class <class_name>:
    <attr_name>: <type>
    <attr_name>: <type> = <default_value>
    <attr_name>: list/dict/set = field(default_factory=list/dict/set)
```
* **Objects can be made [sortable](#sortable) with `'order=True'` and immutable with `'frozen=True'`.**
* **For object to be [hashable](#hashable), all attributes must be hashable and 'frozen' must be True.**
* **Function field() is needed because `'<attr_name>: list = []'` would make a list that is shared among all instances. Its 'default_factory' argument can be any [callable](#callable).**
* **For attributes of arbitrary type use `'typing.Any'`.**

#### Inline:
```python
from dataclasses import make_dataclass
<class> = make_dataclass('<class_name>', <coll_of_attribute_names>)
<class> = make_dataclass('<class_name>', <coll_of_tuples>)
<tuple> = ('<attr_name>', <type> [, <default_value>])
```

#### Rest of type annotations (CPython interpreter ignores them all):
```python
import collections.abc as abc, typing as tp
<var_name>: list/set/abc.Iterable/abc.Sequence/tp.Optional[<type>] [= <obj>]
<var_name>: dict/tuple/tp.Union[<type>, ...] [= <obj>]
def func(<arg_name>: <type> [= <obj>]) -> <type>: ...
```

### Slots
**Mechanism that restricts objects to attributes listed in 'slots' and significantly reduces their memory footprint.**

```python
class MyClassWithSlots:
    __slots__ = ['a']
    def __init__(self):
        self.a = 1
```

### Copy
```python
from copy import copy, deepcopy
<object> = copy(<object>)
<object> = deepcopy(<object>)
```


Duck Types
----------
**A duck type is an implicit type that prescribes a set of special methods. Any object that has those methods defined is considered a member of that duck type.**

### Comparable
* **If eq() method is not overridden, it returns `'id(self) == id(other)'`, which is the same as `'self is other'`.**
* **That means all objects compare not equal by default.**
* **Only the left side object has eq() method called, unless it returns NotImplemented, in which case the right object is consulted. False is returned if both return NotImplemented.**
* **Ne() automatically works on any object that has eq() defined.**

```python
class MyComparable:
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.a == other.a
        return NotImplemented
```

### Hashable
* **Hashable object needs both hash() and eq() methods and its hash value should never change.**
* **Hashable objects that compare equal must have the same hash value, meaning default hash() that returns `'id(self)'` will not do.**
* **That is why Python automatically makes classes unhashable if you only implement eq().**

```python
class MyHashable:
    def __init__(self, a):
        self._a = a
    @property
    def a(self):
        return self._a
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.a == other.a
        return NotImplemented
    def __hash__(self):
        return hash(self.a)
```

### Sortable
* **With 'total_ordering' decorator, you only need to provide eq() and one of lt(), gt(), le() or ge() special methods and the rest will be automatically generated.**
* **Functions sorted() and min() only require lt() method, while max() only requires gt(). However, it is best to define them all so that confusion doesn't arise in other contexts.**
* **When two lists, strings or dataclasses are compared, their values get compared in order until a pair of unequal values is found. The comparison of this two values is then returned. The shorter sequence is considered smaller in case of all values being equal.**
* **For proper alphabetical order pass `'key=locale.strxfrm'` to sorted() after running `'locale.setlocale(locale.LC_COLLATE, "en_US.UTF-8")'`.**

```python
from functools import total_ordering

@total_ordering
class MySortable:
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.a == other.a
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.a < other.a
        return NotImplemented
```

### Iterator
* **Any object that has methods next() and iter() is an iterator.**
* **Next() should return next item or raise StopIteration exception.**
* **Iter() should return 'self'.**
```python
class Counter:
    def __init__(self):
        self.i = 0
    def __next__(self):
        self.i += 1
        return self.i
    def __iter__(self):
        return self
```

```python
>>> counter = Counter()
>>> next(counter), next(counter), next(counter)
(1, 2, 3)
```

#### Python has many different iterator objects:
* **Sequence iterators returned by the [iter()](#iterator) function, such as list\_iterator and set\_iterator.**
* **Objects returned by the [itertools](#itertools) module, such as count, repeat and cycle.**
* **Generators returned by the [generator functions](#generator) and [generator expressions](#comprehensions).**
* **File objects returned by the [open()](#open) function, etc.**

### Callable
* **All functions and classes have a call() method, hence are callable.**
* **When this cheatsheet uses `'<function>'` as an argument, it actually means `'<callable>'`.**
```python
class Counter:
    def __init__(self):
        self.i = 0
    def __call__(self):
        self.i += 1
        return self.i
```

```python
>>> counter = Counter()
>>> counter(), counter(), counter()
(1, 2, 3)
```

### Context Manager
* **With statements only work with objects that have enter() and exit() special methods.**
* **Enter() should lock the resources and optionally return an object.**
* **Exit() should release the resources.**
* **Any exception that happens inside the with block is passed to the exit() method.**
* **The exit() method can suppress the exception by returning a true value.**
```python
class MyOpen:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename)
        return self.file
    def __exit__(self, exc_type, exception, traceback):
        self.file.close()
```

```python
>>> with open('test.txt', 'w') as file:
...     file.write('Hello World!')
>>> with MyOpen('test.txt') as file:
...     print(file.read())
Hello World!
```


Iterable Duck Types
-------------------
### Iterable
* **Only required method is iter(). It should return an iterator of object's items.**
* **Contains() automatically works on any object that has iter() defined.**
```python
class MyIterable:
    def __init__(self, a):
        self.a = a
    def __iter__(self):
        return iter(self.a)
    def __contains__(self, el):
        return el in self.a
```

```python
>>> obj = MyIterable([1, 2, 3])
>>> [el for el in obj]
[1, 2, 3]
>>> 1 in obj
True
```

### Collection
* **Only required methods are iter() and len(). Len() should return the number of items.**
* **This cheatsheet actually means `'<iterable>'` when it uses `'<collection>'`.**
* **I chose not to use the name 'iterable' because it sounds scarier and more vague than 'collection'. The only drawback of this decision is that the reader could think a certain function doesn't accept iterators when it does, since iterators are the only built-in objects that are iterable but are not collections.**
```python
class MyCollection:
    def __init__(self, a):
        self.a = a
    def __iter__(self):
        return iter(self.a)
    def __contains__(self, el):
        return el in self.a
    def __len__(self):
        return len(self.a)
```


Enum
----
```python
from enum import Enum, auto
```

```python
class <enum_name>(Enum):
    <member_name> = auto()
    <member_name> = <value>
    <member_name> = <value>, <value>
```
* **Function auto() returns an increment of the last numeric value or 1.**
* **Accessing a member named after a reserved keyword causes SyntaxError.**
* **Methods receive the member they were called on as the 'self' argument.**

```python
<member> = <enum>.<member_name>           # Returns a member.
<member> = <enum>['<member_name>']        # Returns a member. Raises KeyError.
<member> = <enum>(<value>)                # Returns a member. Raises ValueError.
<str>    = <member>.name                  # Returns member's name.
<obj>    = <member>.value                 # Returns member's value.
```

```python
<list>   = list(<enum>)                   # Returns enum's members.
<list>   = [a.name for a in <enum>]       # Returns enum's member names.
<list>   = [a.value for a in <enum>]      # Returns enum's member values.
<member> = random.choice(list(<enum>))    # Returns a random member.
```

```python
def get_next_member(member):
    members = list(type(member))
    index = members.index(member) + 1
    return members[index % len(members)]
```

### Inline
```python
Cutlery = Enum('Cutlery', 'FORK KNIFE SPOON')
Cutlery = Enum('Cutlery', ['FORK', 'KNIFE', 'SPOON'])
Cutlery = Enum('Cutlery', {'FORK': 1, 'KNIFE': 2, 'SPOON': 3})
```

#### User-defined functions cannot be values, so they must be wrapped:
```python
from functools import partial
LogicOp = Enum('LogicOp', {'AND': partial(lambda l, r: l and r),
                           'OR':  partial(lambda l, r: l or r)})
```


Exceptions
----------
```python
try:
    <code>
except <exception>:
    <code>
```

### Complex Example
```python
try:
    <code_1>
except <exception_a>:
    <code_2_a>
except <exception_b>:
    <code_2_b>
else:
    <code_2_c>
finally:
    <code_3>
```
* **Code inside the `'else'` block will only be executed if `'try'` block had no exceptions.**
* **Code inside the `'finally'` block will always be executed (unless a signal is received).**
* **All variables that are initialized in executed blocks are also visible in all subsequent blocks, as well as outside the try/except clause (only function block delimits scope).**
* **To catch signals use `'signal.signal(signal_number, <func>)'`.**

### Catching Exceptions
```python
except <exception>: ...
except <exception> as <name>: ...
except (<exception>, [...]): ...
except (<exception>, [...]) as <name>: ...
```
* **Also catches subclasses of the exception.**
* **Use `'traceback.print_exc()'` to print the error message to stderr.**
* **Use `'print(<name>)'` to print just the cause of the exception (its arguments).**
* **Use `'logging.exception(<message>)'` to log the passed message, followed by the full error message of the caught exception.**

### Raising Exceptions
```python
raise <exception>
raise <exception>()
raise <exception>(<el> [, ...])
```

#### Re-raising caught exception:
```python
except <exception> [as <name>]:
    ...
    raise
```

### Built-in Exceptions
```text
BaseException
 +-- SystemExit                   # Raised by the sys.exit() function.
 +-- KeyboardInterrupt            # Raised when the user hits the interrupt key (ctrl-c).
 +-- Exception                    # User-defined exceptions should be derived from this class.
      +-- ArithmeticError         # Base class for arithmetic errors such as ZeroDivisionError.
      +-- AssertionError          # Raised by `assert <exp>` if expression returns false value.
      +-- AttributeError          # Raised when object doesn't have requested attribute/method.
      +-- EOFError                # Raised by input() when it hits an end-of-file condition.
      +-- LookupError             # Base class for errors when a collection can't find an item.
      |    +-- IndexError         # Raised when a sequence index is out of range.
      |    +-- KeyError           # Raised when a dictionary key or set element is missing.
      +-- MemoryError             # Out of memory. Could be too late to start deleting vars.
      +-- NameError               # Raised when nonexistent name (variable/func/class) is used.
      |    +-- UnboundLocalError  # Raised when local name is used before it's being defined.
      +-- OSError                 # Errors such as FileExistsError/PermissionError (see #Open).
      |    +-- ConnectionError    # Errors such as BrokenPipeError/ConnectionAbortedError.
      +-- RuntimeError            # Raised by errors that don't fall into other categories.
      |    +-- NotImplementedErr  # Can be raised by abstract methods or by unfinished code.
      |    +-- RecursionError     # Raised when the maximum recursion depth is exceeded.
      +-- StopIteration           # Raised by next() when run on an empty iterator.
      +-- TypeError               # Raised when an argument is of the wrong type.
      +-- ValueError              # When argument has the right type but inappropriate value.
```

#### Collections and their exceptions:
```text
+-----------+------------+------------+------------+
|           |    List    |    Set     |    Dict    |
+-----------+------------+------------+------------+
| getitem() | IndexError |            |  KeyError  |
| pop()     | IndexError |  KeyError  |  KeyError  |
| remove()  | ValueError |  KeyError  |            |
| index()   | ValueError |            |            |
+-----------+------------+------------+------------+
```

#### Useful built-in exceptions:
```python
raise TypeError('Argument is of the wrong type!')
raise ValueError('Argument has the right type but an inappropriate value!')
raise RuntimeError('None of above!')
```

### User-defined Exceptions
```python
class MyError(Exception): pass
class MyInputError(MyError): pass
```


Exit
----
**Exits the interpreter by raising SystemExit exception.**
```python
import sys
sys.exit()                        # Exits with exit code 0 (success).
sys.exit(<el>)                    # Prints to stderr and exits with 1.
sys.exit(<int>)                   # Exits with the passed exit code.
```


Print
-----
```python
print(<el_1>, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```
* **Use `'file=sys.stderr'` for messages about errors.**
* **Use `'flush=True'` to forcibly flush the stream.**

### Pretty Print
```python
from pprint import pprint
pprint(<collection>, width=80, depth=None, compact=False, sort_dicts=True)
```
* **Levels deeper than 'depth' get replaced by '...'.**


Input
-----
**Reads a line from the user input or pipe if present.**

```python
<str> = input(prompt=None)
```
* **Trailing newline gets stripped.**
* **Prompt string is printed to the standard output before reading input.**
* **Raises EOFError when user hits EOF (ctrl-d/ctrl-z⏎) or input stream gets exhausted.**


Open
----
**Opens the file and returns a corresponding file object.**

```python
<file> = open(<path>, mode='r', encoding=None, newline=None)
```
* **`'encoding=None'` means that the default encoding is used, which is platform dependent. Best practice is to use `'encoding="utf-8"'` whenever possible.**
* **`'newline=None'` means all different end of line combinations are converted to '\n' on read, while on write all '\n' characters are converted to system's default line separator.**
* **`'newline=""'` means no conversions take place, but input is still broken into chunks by readline() and readlines() on every '\n', '\r' and '\r\n'.**

### Modes
* **`'r'`  - Read (default).**
* **`'w'`  - Write (truncate).**
* **`'x'`  - Write or fail if the file already exists.**
* **`'a'`  - Append.**
* **`'w+'` - Read and write (truncate).**
* **`'r+'` - Read and write from the start.**
* **`'a+'` - Read and write from the end.**
* **`'t'`  - Text mode (default).**
* **`'b'`  - Binary mode (`'br'`, `'bw'`, `'bx'`, …).**

### Exceptions
* **`'FileNotFoundError'` can be raised when reading with `'r'` or `'r+'`.**
* **`'FileExistsError'` can be raised when writing with `'x'`.**
* **`'IsADirectoryError'` and `'PermissionError'` can be raised by any.**
* **`'OSError'` is the parent class of all listed exceptions.**

### File Object
```python
<file>.seek(0)                      # Moves to the start of the file.
<file>.seek(offset)                 # Moves 'offset' chars/bytes from the start.
<file>.seek(0, 2)                   # Moves to the end of the file.
<bin_file>.seek(±offset, <anchor>)  # Anchor: 0 start, 1 current position, 2 end.
```

```python
<str/bytes> = <file>.read(size=-1)  # Reads 'size' chars/bytes or until EOF.
<str/bytes> = <file>.readline()     # Returns a line or empty string/bytes on EOF.
<list>      = <file>.readlines()    # Returns a list of remaining lines.
<str/bytes> = next(<file>)          # Returns a line using buffer. Do not mix.
```

```python
<file>.write(<str/bytes>)           # Writes a string or bytes object.
<file>.writelines(<collection>)     # Writes a coll. of strings or bytes objects.
<file>.flush()                      # Flushes write buffer. Runs every 4096/8192 B.
```
* **Methods do not add or strip trailing newlines, not even writelines().**

### Read Text from File
```python
def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()
```

### Write Text to File
```python
def write_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
```


OS Commands
-----------
```python
import os, shutil, subprocess
```

```python
os.chdir(<path>)                    # Changes the current working directory.
os.mkdir(<path>, mode=0o777)        # Creates a directory. Permissions are in octal.
os.makedirs(<path>, mode=0o777)     # Creates all path's dirs. Also `exist_ok=False`.
```

```python
shutil.copy(from, to)               # Copies the file. 'to' can exist or be a dir.
shutil.copy2(from, to)              # Also copies creation and modification time.
shutil.copytree(from, to)           # Copies the directory. 'to' must not exist.
```

```python
os.rename(from, to)                 # Renames/moves the file or directory.
os.replace(from, to)                # Same, but overwrites file 'to' even on Windows.
shutil.move(from, to)               # Rename() that moves into 'to' if it's a dir.
```

```python
os.remove(<path>)                   # Deletes the file.
os.rmdir(<path>)                    # Deletes the empty directory.
shutil.rmtree(<path>)               # Deletes the directory.
```
* **Paths can be either strings, Paths or DirEntry objects.**
* **Functions report OS related errors by raising either OSError or one of its [subclasses](#exceptions-1).**

### Shell Commands
```python
<pipe> = os.popen('<command>')      # Executes command in sh/cmd. Returns its stdout pipe.
<str>  = <pipe>.read(size=-1)       # Reads 'size' chars or until EOF. Also readline/s().
<int>  = <pipe>.close()             # Closes the pipe. Returns None on success (returncode 0).
```

#### Sends '1 + 1' to the basic calculator and captures its output:
```python
>>> subprocess.run('bc', input='1 + 1\n', capture_output=True, text=True)
CompletedProcess(args='bc', returncode=0, stdout='2\n', stderr='')
```

#### Sends test.in to the basic calculator running in standard mode and saves its output to test.out:
```python
>>> from shlex import split
>>> os.popen('echo 1 + 1 > test.in')
>>> subprocess.run(split('bc -s'), stdin=open('test.in'), stdout=open('test.out', 'w'))
CompletedProcess(args=['bc', '-s'], returncode=0)
>>> open('test.out').read()
'2\n'
```


JSON
----
**Text file format for storing collections of strings and numbers.**

```python
import json
<str>    = json.dumps(<object>)     # Converts object to JSON string.
<object> = json.loads(<str>)        # Converts JSON string to object.
```

### Read Object from JSON File
```python
def read_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
```

### Write Object to JSON File
```python
def write_to_json_file(filename, an_object):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(an_object, file, ensure_ascii=False, indent=2)
```


Pickle
------
**Binary file format for storing Python objects.**

```python
import pickle
<bytes>  = pickle.dumps(<object>)   # Converts object to bytes object.
<object> = pickle.loads(<bytes>)    # Converts bytes object to object.
```

### Read Object from File
```python
def read_pickle_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
```

### Write Object to File
```python
def write_to_pickle_file(filename, an_object):
    with open(filename, 'wb') as file:
        pickle.dump(an_object, file)
```


CSV
---
**Text file format for storing spreadsheets.**

```python
import csv
```

### Read
```python
<reader> = csv.reader(<file>)       # Also: `dialect='excel', delimiter=','`.
<list>   = next(<reader>)           # Returns next row as a list of strings.
<list>   = list(<reader>)           # Returns a list of remaining rows.
```
* **File must be opened with a `'newline=""'` argument, or newlines embedded inside quoted fields will not be interpreted correctly!**
* **To print the spreadsheet to the console use [Tabulate](#table) library.**
* **For XML and binary Excel files (xlsx, xlsm and xlsb) use [Pandas](#dataframe-plot-encode-decode) library.**
* **Reader accepts any iterator of strings, not just files.**

### Write
```python
<writer> = csv.writer(<file>)       # Also: `dialect='excel', delimiter=','`.
<writer>.writerow(<collection>)     # Encodes objects using `str(<el>)`.
<writer>.writerows(<coll_of_coll>)  # Appends multiple rows.
```
* **File must be opened with a `'newline=""'` argument, or '\r' will be added in front of every '\n' on platforms that use '\r\n' line endings!**
* **Open existing file with `'mode="w"'` to overwrite it or `'mode="a"'` to append to it.**

### Parameters
* **`'dialect'` - Master parameter that sets the default values. String or a 'csv.Dialect' object.**
* **`'delimiter'` - A one-character string used to separate fields.**
* **`'quotechar'` - Character for quoting fields that contain special characters.**
* **`'doublequote'` - Whether quotechars inside fields are/get doubled or escaped.**
* **`'skipinitialspace'` - Is space character at the start of the field stripped by the reader.**
* **`'lineterminator'` - How writer terminates rows. Reader is hardcoded to '\n', '\r', '\r\n'.**
* **`'quoting'` - 0: As necessary, 1: All, 2: All but numbers which are read as floats, 3: None.**
* **`'escapechar'` - Character for escaping quotechars if 'doublequote' is False.**

### Dialects
```text
+------------------+--------------+--------------+--------------+
|                  |     excel    |   excel-tab  |     unix     |
+------------------+--------------+--------------+--------------+
| delimiter        |       ','    |      '\t'    |       ','    |
| quotechar        |       '"'    |       '"'    |       '"'    |
| doublequote      |      True    |      True    |      True    |
| skipinitialspace |     False    |     False    |     False    |
| lineterminator   |    '\r\n'    |    '\r\n'    |      '\n'    |
| quoting          |         0    |         0    |         1    |
| escapechar       |      None    |      None    |      None    |
+------------------+--------------+--------------+--------------+
```

### Read Rows from CSV File
```python
def read_csv_file(filename, dialect='excel', **params):
    with open(filename, encoding='utf-8', newline='') as file:
        return list(csv.reader(file, dialect, **params))
```

### Write Rows to CSV File
```python
def write_to_csv_file(filename, rows, mode='w', dialect='excel', **params):
    with open(filename, mode, encoding='utf-8', newline='') as file:
        writer = csv.writer(file, dialect, **params)
        writer.writerows(rows)
```



Metaprogramming
---------------
**Code that generates code.**

### Type
**Type is the root class. If only passed an object it returns its type (class). Otherwise it creates a new class.**

```python
<class> = type('<class_name>', <tuple_of_parents>, <dict_of_class_attributes>)
```

```python
>>> Z = type('Z', (), {'a': 'abcde', 'b': 12345})
>>> z = Z()
```

### Meta Class
**A class that creates classes.**

```python
def my_meta_class(name, parents, attrs):
    attrs['a'] = 'abcde'
    return type(name, parents, attrs)
```

#### Or:
```python
class MyMetaClass(type):
    def __new__(cls, name, parents, attrs):
        attrs['a'] = 'abcde'
        return type.__new__(cls, name, parents, attrs)
```
* **New() is a class method that gets called before init(). If it returns an instance of its class, then that instance gets passed to init() as a 'self' argument.**
* **It receives the same arguments as init(), except for the first one that specifies the desired type of the returned instance (MyMetaClass in our case).**
* **Like in our case, new() can also be called directly, usually from a new() method of a child class (**`def __new__(cls): return super().__new__(cls)`**).**
* **The only difference between the examples above is that my\_meta\_class() returns a class of type type, while MyMetaClass() returns a class of type MyMetaClass.**

### Metaclass Attribute
**Right before a class is created it checks if it has the 'metaclass' attribute defined. If not, it recursively checks if any of its parents has it defined and eventually comes to type().**

```python
class MyClass(metaclass=MyMetaClass):
    b = 12345
```

```python
>>> MyClass.a, MyClass.b
('abcde', 12345)
```

### Type Diagram
```python
type(MyClass) == MyMetaClass         # MyClass is an instance of MyMetaClass.
type(MyMetaClass) == type            # MyMetaClass is an instance of type.
```

```text
+-------------+-------------+
|   Classes   | Metaclasses |
+-------------+-------------|
|   MyClass <-- MyMetaClass |
|             |     ^       |
|    object <----- type <+  |
|             |     | +--+  |
|     str <---------+       |
+-------------+-------------+
```

### Inheritance Diagram
```python
MyClass.__base__ == object           # MyClass is a subclass of object.
MyMetaClass.__base__ == type         # MyMetaClass is a subclass of type.
```

```text
+-------------+-------------+
|   Classes   | Metaclasses |
+-------------+-------------|
|   MyClass   | MyMetaClass |
|      ^      |     ^       |
|    object -----> type     |
|      v      |             |
|     str     |             |
+-------------+-------------+
```


Eval
----
```python
>>> from ast import literal_eval
>>> literal_eval('[1, 2, 3]')
[1, 2, 3]
>>> literal_eval('1 + 2')
ValueError: malformed node or string
```




Libraries
=========


Scraping
--------
#### Scrapes Python's URL and logo from its Wikipedia page:
```python
# $ pip3 install requests beautifulsoup4
import requests, bs4, os, sys

try:
    response   = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
    document   = bs4.BeautifulSoup(response.text, 'html.parser')
    table      = document.find('table', class_='infobox vevent')
    python_url = table.find('th', text='Website').next_sibling.a['href']
    logo_url   = table.find('img')['src']
    logo       = requests.get(f'https:{logo_url}').content
    filename   = os.path.basename(logo_url)
    with open(filename, 'wb') as file:
        file.write(logo)
    print(f'{python_url}, file://{os.path.abspath(filename)}')
except requests.exceptions.ConnectionError:
    print("You've got problems with connection.", file=sys.stderr)
```





PySimpleGUI
-----------
```python
# $ pip3 install PySimpleGUI
import PySimpleGUI as sg

layout = [[sg.Text("What's your name?")], [sg.Input()], [sg.Button('Ok')]]
window = sg.Window('Window Title', layout)
event, values = window.read()
print(f'Hello {values[0]}!' if event == 'Ok' else '')
```


### Virtual Environments
**System for installing libraries directly into project's directory.**

```bash
$ python3 -m venv <name>      # Creates virtual environment in current directory.
$ source <name>/bin/activate  # Activates venv. On Windows run `<name>\Scripts\activate`.
$ pip3 install <library>      # Installs the library into active environment.
$ python3 <path>              # Runs the script in active environment. Also `./<path>`.
$ deactivate                  # Deactivates the active virtual environment.
```

### Basic Script Template
```python
#!/usr/bin/env python3
#
# Usage: .py
#

from sys import argv, exit
from collections import defaultdict, namedtuple
from dataclasses import make_dataclass
from enum import Enum
import functools as ft, itertools as it, operator as op, re


def main():
    pass


###
##  UTIL
#

def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()


if __name__ == '__main__':
    main()
```

