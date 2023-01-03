![ALX](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
> python classes quizes

### Question #0
```
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.is_new

```
* [ ] False
* [ ] is_new
* [ ] Nothing 
* [X] True