![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
> Test Driven Developement 

![Test](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/246/giphy-4.gif)

## Intro 
Starting from today:
- Based on the requirements of each task, __you should always write the documentation (module(s) + function(s)) and tests first__, before you actually code anything

- The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases

- We strongly encourage you to work together on test cases, so that you don’t miss any edge case. __But not in the implementation of them!__

- __Don’t trust the user__, always think about all possible edge cases


## Resources
1. [doctest- Test interactive python examples](https://docs.python.org/3.4/library/doctest.html)
2. [doctets - Testing through documentation](https://pymotw.com/3/doctest/)
3. [unit tests in python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)
4. [unittest module](https://www.youtube.com/watch?v=6tNS--WetLI)
5. [Interactive and non-interactive tests](https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/)

## Learning objectives
By the end of this session, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) the following concepts without the help of Google.

* [X] What’s an interactive test
* [X] Why tests are important
* [X] How to write Docstrings to create tests
* [X] How to write documentation for each module and function
* [X] What are the basic option flags to create tests
* [X] How to find edge cases

## More info
### Documentation is mandatory
Each module, class, and method must contain docstring as comments see [example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

### Script requirements
- Allowed editors: ```vi```, ```vim```, ```emacs```
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using ```wc```
- All your modules should have a documentation (```python3 -c 'print(__import__("my_module").__doc__)'```)
- All your classes should have a documentation (```python3 -c 'print(__import__("my_module").MyClass.__doc__)'```)
- All your functions (inside and outside a class) should have a documentation (```python3 -c 'print(__import__("my_module").my_function.__doc__)'``` and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'```)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python test cases
- All your files should end with a new line
- All your test files should be inside a folder ```tests```
- All your test files should be text files (extension: ```.txt```)
- All your tests should be executed by using this command: 
```bash
python3 -m doctest ./tests/*
```
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (```python3 -c 'print(__import__("my_module").my_function.__doc__)'```)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

[Quizes](./quiz.md)