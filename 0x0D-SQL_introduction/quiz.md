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
