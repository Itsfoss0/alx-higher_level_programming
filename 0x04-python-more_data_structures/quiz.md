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

#### Question #5
What do these lines print?
```
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('age')
```
* [ ] 89
* [ ] age
* [ ] Not found
* [X] Nothing
* [ ] 12

#### Question #6
What do these lines print?
```
>>> a = { 'id': 89, 'name': "John" }
>>> a['id']
```
* [ ] a['id']
* [ ] id
* [ ] 'id'
* [ ] John
* [X] 89

#### Question #7
What do these lines print?
```
>>> for i in [1, 3, 4, 2]:
>>>     print(i, end=" ")
```
* [X] 1 2 3 4 
* [ ] 0 1 2 3
* [ ] 1 2 3 4
* [ ] 1 2 4 3 0 

#### Question #8
What do these lines print?
```
>>> for i in [1, 2, 3, 4]:
>>>     print(i, end=" ")
```
* [ ] 1 2 3 
* [ ] 0 1 2 3
* [ ] 0 1 2 3 5 
* [X] 1 2 3 4

#### Question #9
What do these lines print?
```
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
>>> a.get('projects')[3]
```
* [ ] 1 2 3 4
* [X] 4
* [ ] [4]
* [ ] [3]
* [ ] 3


#### Question #10
What do these line print?
```
>>> for i in range(1, 4):
>>>     print(i, end=" ")
```
* [ ] 1 2 3 4
* [X] 1 2 3
* [ ] 0 1 2 3

#### Question #11
What do these lines print?
```
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('age', 0)
```
* [X] 0 
* [ ] 'age'
* [ ] Nothing
* [ ] 89