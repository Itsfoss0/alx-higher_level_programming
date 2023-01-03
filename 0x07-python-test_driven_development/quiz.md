![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
> Test driven development quizes

### Question #0
Is this module correctly documented?
```python
#!/usr/bin/python3
""" 
    My calculation module
"""
import sys
...

```
* [X] Yes
* [ ] No 


### Question #1
Based on this code, what should all the test cases be? (select multiple)
```python 
def uniq(list):
    """ Returns unique values of a list """
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list

```
* [X] list with 2 different element (same type)
* [X] not a list argument (ex: passing a dictionary to the method)
* [X] list with more than 2 times the same element (same type)
* [X] list with one element (any type)
* [X] empty list
* [X] list with multiple types (integer, string, etc…)
* [X] list with twice the same element (same type)


### Question #2
Is this a standardized way to comment a function in Python?
```python
"""" Addition function """
def add(a, b):
    return a + b

```
* [ ] Yes
* [X] No


### Question #3
Is this a standardized way to comment a function in Python?

```python 
##########
# Addition function
##########
def add(a, b):
    return a + b

```
* [ ] Yes
* [X] No


### Question #4
Is this a standardized way to comment a function in Python?
```python
/* Addition function */
def add(a, b):
    return a + b

```
* [ ] Yes
* [X] No

### Question #5
Is this module correctly commented?
```python
#!/usr/bin/python3
import sys

""" 
    My calculation module
"""
...

```
* [ ] Yes
* [X] No
> ### Tips 
> Docstrings must be bofore import statments

### Question #6
Is this a standardized way to comment a function in Python?
```python
def add(a, b):
    """ Addition function """
    return a + b
```
* [X] Yes
* [ ] No