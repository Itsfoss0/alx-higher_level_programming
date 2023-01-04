![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
>  Set, dictionary, map and filter quizes 

#### Question #0
What do these lines print?
```
>>> for i in ["Hello", "Holberton", "School", 98]:
>>>     print(i, end=" ")
```
* [X] Hello Holberton School 98
* [ ] 0 1 2 3
* [ ] 1 2 3 4 

#### Question #1
What do these lines print?
```
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
>>> a.get('projects')
```
* [ ] [1]
* [ ] 'projects'
* [X] 1 2 3 4 
* [ ] Nothing
* [ ] list

#### Question #2
What do these lines print?
```
>>> for i in range(0, 3):
>>>     print(i, end=" ")
```
* [X] 0 1 2 
* [ ] 1 2 3 
* [ ] 0 1 2 3

#### Question #3
What do these lines print?
```
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
>>> a.get('friends')[-1].get("name")
```
* [X] Amy
* [ ] 89
* [ ] [ { ‘id’: 82, ‘name’: “Bob” }, { ‘id’: 83, ‘name’: “Amy” } ]
* [ ] Nothing
* [ ] Bob

#### Question #4
What do these lines print?
```
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('id')
```
* [ ] a['id']
* [ ] id
* [ ] 'id'
* [ ] John
* [X] 89
