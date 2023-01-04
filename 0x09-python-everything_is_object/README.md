![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
> Everything object

![meme](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg)

## Background Context
Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:
```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>> 
```

OK, But what about this?
```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 
```
![meme](https://media.giphy.com/media/wAjfQ9MLUfFjq/giphy.gif)

## Resources
1. [Objects and Values](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
2. [Aliasing](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
3. [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
4. [Mutation](http://composingprograms.com/pages/24-mutable-data.html#sequence-objects)
5. [Cloning lists](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
6. [Python tuples - Immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)

## Learning objectives
By the end of this project, you should be able to [explain](https://fs.blog/feynman-learning-technique/) to anyone the following concepts without the help of Google.

* [X] What is an object
* [X] What is the difference between a class and an object or instance
* [X] What is the difference between immutable object and mutable object
* [X] What is a reference
* [X] What is an assignment
* [X] What is an alias
* [X] How to know if two variables are identical
* [X] How to know if two variables are linked to the same object
* [X] How to display the variable identifier (which is the memory address in the CPython implementation)
* [X] What is mutable and immutable
* [X] What are the built-in mutable types
* [X] What are the built-in immutable types
* [X] How does Python pass variables to functions