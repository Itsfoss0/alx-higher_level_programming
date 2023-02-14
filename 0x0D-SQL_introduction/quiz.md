![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

## Quizes

##### Quiz #0
How do you list all ```users``` in this table
```sql
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```
* [ ] SELECT ALL users;
* [ ] DELETE * FROM users;
* [X] SELECT * FROM users;

#### Question #1
How do you change the name of ```users``` with the record ```id = 89``` to ```Holberton```

```sql
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```

* [ ] UPDATE users SET name = “Holberton”;
* [X] UPDATE users SET name = “Holberton” WHERE id = 89;
* [ ] CHANGE users SET name = “Holberton” WHERE id = 89;


#### Question #2
How do you delete the users record with id = 89 in this table?

```sql
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```
* [ ] DELETE FROM users;
* [ ] DELETE users WHERE id = 89;
* [X] DELETE FROM users WHERE id = 89;
* [ ] DELETE FROM users WHERE id IS EQUAL TO 89;

#### Question #3
What is a relational database? (please select all correct answers)

* [ ] married databases
* [X] a table containing only one object representation
* [ ] data are organized by tables and indexes
* [X] a collection of data
* [X] a database
* [ ] a table containing multiple object representation
* [X] data are organized by tables, records and columns

#### Question #4
What does DDL stand for?

* [ ] Data Document Language
* [X] Data Definition Language
* [ ] Database Definition Language
* [ ] Document Data Language

#### Question #5
What does SQL stand for?

* [ ] Solid Query Language
* [ ] Sequences of Query Logic
* [X] Structured Query Language
* [ ] Structured Question Language

#### Question #6
How do you add a new record into the table ```users```?

```sql
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```
* [X] INSERT INTO users (id, name, age) VALUES (2, “Betty”, 30);
* [ ] INSERT users (id, name, age) VALUES (2, “Betty”, 30);
* [ ] INSERT INTO users (id, name) VALUES (2, “Betty”, 30);
* [ ] INSERT INTO users (id, name, age) VALUES (2, “Betty”);

#### Question #7
How do you list all ```users``` records with ```age > 21``` in this table

```sql
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
```
* [X] SELECT * FROM users WHERE age > 21;
* [ ] SELECT * FROM users WHERE age < 21;
* [ ] SELECT * FROM users WHERE age IS UP TO 21;
* [ ] SELECT * FROM users WHERE age BETWEEN 21 AND 89;

#### Question #8
What does DML stand for?

* [X] Data Manipulation Language
* [ ] Database Manipulation Language
* [ ] Document Manipulation Language
* [ ] Document Model Language
