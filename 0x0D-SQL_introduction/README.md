![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

![sql-meme](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg)

## About
SQL! Structured Query Language (SQL) is a programming language that is widely used for managing and manipulating relational databases. With its ability to extract valuable insights and data from large and complex databases, SQL has become an essential tool for businesses of all sizes. In this project, we'll dive into the basics of SQL, its key features and benefits, and how you can use it to manage your own databases. Whether you're a beginner or an experienced user, this project will provide you with a comprehensive overview of SQL and its applications. So, let's get started!

## Resources
__Read or watch__ 
1. [What is a Database & SQL](https://www.youtube.com/watch?v=FR4QIeZaPeM)
2. [Basic mySQL tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
3. [Basic SQL statments DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
4. [Basic Queries SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
6. [SQL techniques: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
7. [SQL techniques: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
8. [What makes a big difference between backticks and apostrophe](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
9. [MySQL cheatsheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
10. [MySQL 8.0 Statement syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
11. [Installing MySQL on ubuntu](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)

## Learning objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) the following concepts without the help of __Google__

* [X] What’s a database
* [X] What’s a relational database
* [X] What does SQL stand for
* [X] What’s MySQL
* [X] How to create a database in MySQL
* [X] What does DDL and DML stand for
* [X] How to CREATE or ALTER a table
* [X] How to SELECT data from a table
* [X] How to INSERT, UPDATE or DELETE data
* [X] What are subqueries
* [X] How to use MySQL functions

## More info
### Comments for your SQL files

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

### Install MySQL 8.0 on Ubuntu 20.04 LTS

```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

### Connect to your MySQL server
```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```
## Quizes
[Quiz](./quiz.md)