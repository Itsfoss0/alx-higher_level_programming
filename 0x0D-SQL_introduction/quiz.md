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
