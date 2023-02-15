![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

![sql-join-meme](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg)

## About 
While SQL is a powerful language for managing data, it also has many intermediate concepts that can be used to create more complex and nuanced queries. Example of such include __Joins__, __Subqueries__ , __Aggregate Functions__ __Window Functions__, __Views__ and __Stored Procedures__ Lets explore the most common of them in this project. 

## Resources
1. [How to create a new user and assing permission in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
2. [How to use MySQL GRANT statement to assign permissions to users](https://www.mysqltutorial.org/mysql-grant.aspx)
3. [MySQL constraits](https://zetcode.com/mysql/constraints/)
4. [SQL techniques: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
5. [SQL techniques: join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
6. [SQL techniqes: multiple joins and the disctint keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)
7. [SQL techniques: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
8. [SQL techniques: unions and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)
9. [MySQL cheatsheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
10. [Seven Join types ](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
11. [MySQL tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
12. [SQL style guide](https://www.sqlstyle.guide/)
13. [MySQL 8.0 statement syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

 Extra resources around relational database model design

 [Design](https://www.guru99.com/database-design.html)

 [Normalization](https://www.guru99.com/database-normalization.html)

 [ER modeling](https://www.guru99.com/er-modeling.html)


 ## Learning objectives
 By the end of this project, you are expected to be able to [explain to anyone]() __without the help of Google__

 * [X] How to create a new MySQL user
 * [X] How to manage privileges for a user to a database or table
 * [X] What is a ```PRIMARY KEY ```
 * [X] What’s a ```FOREIGN KEY```
 * [X] How to use ```NOT NULL``` and ```UNIQUE``` constraints
 * [X] How to retrieve datas from multiple tables in one request
 * [X] What are subqueries
 * [X] What are JOIN and UNION

 ## How to import a SQL dump
 ```
 $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
![sql-joins-cheat-sheet](./sql-cheat-sheet.png)

## Quizes
[Quizes](./quiz.md)