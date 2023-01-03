![ALX](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
> python classes quizes

#### Question #0
```
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.is_new

```
* [ ] False
* [ ] is_new
* [ ] Nothing 
* [X] True


#### Question #1
What do these lines print?
```
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.name
```

* [ ] John 
* [ ] None
* [ ] name
* [X] no name


#### Question #2
What do these lines print?
```
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User("John")
>>> u.name
```
* [X] John 
* [ ] no name
* [ ] None
* [ ] name


#### Question #3
In this following code, what is ```id```?
```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
* [ ] A public class method
* [ ] A protected class attribute
* [ ] A private class attribute
* [X] A public class attribute
* [ ] A public instance attribute
* [ ] A public instance method


#### Question #4
In this following code, what is ```__password```?
```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
* [ ] A protected class attribute
* [ ] A private instance attribute
* [X] A private class attribute
* [ ] A public instance attribute
* [ ] A public class attribute
* [ ] A protected instance attribute


#### Question #5
In the following code, what is ```User```
```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
* [ ] An attribute
* [X] A class
* [ ] A string
* [ ] An instance
* [ ] A method

#### Question #6

What do these lines print?
```
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.id
```
* [ ] User.id
* [X] 89
* [ ] Nothing
* [ ] id


#### Question #7
In this following code, what is ```is_new```?
```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```
* [ ] A protected class attribute
* [ ] A private instance attribute
* [ ] A private instance attribute
* [X] A public instance attribute
* [ ] A public class attribute
* [ ] A protected instance attribute 