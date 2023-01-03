![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
> More classes

## Intro
Lets dig a little deeper into classes in python. 

## Resources
Read or watch the following

1. [Object Oriented Programming](https://python.swaroopch.com/oop.html)
2. [OOP in Python](https://python-course.eu/oop/object-oriented-programming.php)(Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: *“General Introduction,”* *“First-class Everything,”* *“A Minimal Class in Python,”* *“Attributes,”* *“Methods,”* *“The ```__init__``` Method,”* *“Data Abstraction, Data Encapsulation, and Information Hiding,”* *“```__str__``` - and ```__repr__``` -Methods,”* *“Public- Protected- and Private Attributes,” & “Destructor”*)
3. [Class vs Instance attributes](https://python-course.eu/oop/class-instance-attributes.php)
4. [Class method vs static methods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
5. [Properties vs setters vs getters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
6. [```__str__``` vs ```__repr__```](https://shipit.dev/posts/python-str-vs-repr.html)

## Learning objectives
By the end of this project, you should be able to [explain](https://fs.blog/feynman-learning-technique/) to anyone the following concepts without the help of Google

* [X] What is OOP
* [X] “first-class everything”
* [X] What is a class
* [X] What is an object and an instance
* [X] What is the difference between a class and an object or instance
* [X] What is an attribute
* [X] What are and how to use public, protected and private attributes
* [X] What is ```self```
* [X] What is a method
* [X] What is the special ```__init__``` method and how to use it
* [X] What is Data Abstraction, Data Encapsulation, and Information Hiding
* [X] What is a property
* [X] What is the difference between an attribute and a property in Python
* [X] What is the Pythonic way to write getters and setters in Python
* [X] What are the special ```__str__``` and ```__repr__``` methods and how to use them
* [X] What is the difference between ```__str__``` and ```__repr__```
* [X] What is a class attribute
* [X] What is the difference between a object attribute and a class attribute
* [X] What is a class method
* [X] What is a static method
* [X] How to dynamically create arbitrary new attributes for existing instances of a class
* [X] How to bind attributes to object and classes
* [X] What is and what does contain ```__dict__``` of a class and of an instance of a class
* [X] How does Python find the attributes of an object or class
* [X] How to use the ```getattr``` function

## Requirements
### General 
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly ```#!/usr/bin/python3```
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version ```2.8.*```)
- All your files must be executable
- The length of your files will be tested using ```wc```

<details>
<summary>Show quiz</summary>

####  Question #0 
What do these lines print?
```python
class User:
    id = 1

User.id = 98
u = User()
u.id = 89
print(User.id)

```
* [ ] 89
* [ ] None
* [X] 98
* [ ] 1 

#### Question #1
What do these lines print?
```python
class User:
    id = 1

u = User()
u.id = 89
User.id = 98
print(u.id)
```
* [X] 89
* [ ] None
* [ ] 1
* [ ] 98

#### Question #2
What is ```__doc__```
* [ ] Creates man file
* [X] The string documentation of an object (based on docstring)
* [ ] Prints the documentation of an object


#### Question #3
What do these lines print?
```python
class User:
    id = 1

u = User()
u.id = 89
print(u.id)
```
* [X] 89
* [ ] 98
* [ ] None
* [ ] 1

#### Question #4
What do these lines print?
```python
class User:
    id = 1

u = User()
print(u.id)
```
* [ ] 89
* [ ] 98
* [ ] None
* [X] 1


#### Question #5
What is ```__str__```
* [ ] Instance method that prints an “informal” and nicely printable string representation of an instance
* [X] Instance method that returns an “informal” and nicely printable string representation of an instance
* [ ] Instance method that returns the dictionary representation of an instance


#### Question #6
What is ```__repr__```
* [ ] Instance method that returns the dictionary representation of an instance
* [ ] Instance method that prints an “official” string representation of an instance
* [X] Instance method that returns an “official” string representation of an instance


#### Question #7
What do these lines print?
```python
class User:
    id = 1

u = User()
u.id = 89
User.id = 98
print(User.id)

```
* [ ] 89
* [ ] None
* [ ] 1
* [X] 98


#### Question #8
What is ```__init__```?
* [X] The instance method called when a new object is created 
* [ ] A class attribute
* [ ] A class method
* [ ] The instance method called when a class is called for the first time


#### Question #9
What do these lines print?
```python
class User:
    id = 1

User.id = 98
u = User()
u.id = 89
print(u.id)
```
* [X] 89
* [ ] 98
* [ ] None
* [ ] 1


#### Question #10
What do these lines print?
```python
class User:
    id = 1

u = User()
User.id = 98
print(u.id)
```
* [ ] 89
* [ ] None
* [ ] 1
* [X] 98


#### Question #11
What do these lines print?
```python
class User:
    id = 1

print(User.id)
```
* [ ] 89
* [X] 1
* [ ] 98
* [ ] None


#### Question #12
What do these lines print
```python
class User:
    id = 1

User.id = 98
u = User()
print(u.id)
```
* [ ] 89
* [ ] None
* [ ] 1
* [X] 98


#### Question #13
What is ```__del__```?
* [X] Instance method called when an instance is deleted
* [ ] Instance method that removes the last character of an instance
* [ ] Instance method that prints the memory address of an instance

</details>