![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

![meme](https://media.makeameme.org/created/orm-supports-eager.jpg)

## About 
Object-Relational Mapping (ORM) is a programming technique that allows developers to interact with a relational database using an object-oriented paradigm in their programming language of choice. In Python, there are several popular ORM libraries, such as SQLAlchemy, Django ORM, and Peewee, which allow developers to interact with databases using Python objects and methods, rather than writing raw SQL queries. ORM libraries can help simplify database interactions, improve code readability, and reduce the amount of boilerplate code required for common database operations.

## Background context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

__Without ORM:__
```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

__With ORM__
```python
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

## Resources
__Read or watch__:
1. [Object-relation mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
2. [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/)(please don’t pay attention to _`_mysql`_)
3. [MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)
4. [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
5. [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
6. [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
7. [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
8. [Flask-SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
9. [10 common stumbling blocks for SQLAlchemy newbies](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
10. [Python SQLAlchemy cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
11. [SQLAlchemy ORM tutorial for python developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)(__Warning__: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)
12. [SQLAlchemy tutorial](https://overiq.com/sqlalchemy-101/)

## Learning objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), __without the help of Google__:

### General 
* [X] Why Python programming is awesome :tada: 
* [X] How to connect to a MySQL database from a Python script
* [X] How to ```SELECT``` rows in a MySQL table from a Python script
* [X] How to ```INSERT``` rows in a MySQL table from a Python script 
* [X] What ORM means
* [X] How to map a Python Class to a MySQL table

## Requirements

- Allowed editors: ```vi```, ```vim```, ```emacs```
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using ```python3``` (version 3.8.5)
- Your files will be executed with ```MySQLdb``` version ```2.0.x```
- Your files will be executed with ```SQLAlchemy``` version ```1.4.x```
- All your files should end with a new line
- The first line of all your files should be exactly ```#!/usr/bin/python3```
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version ```2.8.*```)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation ```(python3 -c 'print(__import__("my_module").__doc__)')```
- All your classes should have a documentation ```(python3 -c 'print(__import__("my_module").MyClass.__doc__)')```
- All your functions (inside and outside a class) should have a documentation ```(python3 -c 'print(__import__("my_module").my_function.__doc__)'``` and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')```
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- You are not allowed to use ```execute``` with sqlalchemy

## More info
### Install ```MySQLdb``` module version 2.0.x
For installing MySQLdb, you need to have MySQL installed: [How to install](https://intranet.alxswe.com/projects/272)

```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```
### Install SQLAlchemy module version 1.4.x
```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```
Also, you can have this Warning message:
```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
```

You can ignore it. 