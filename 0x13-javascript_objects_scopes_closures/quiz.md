![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
> Javascript objects scopes and  closures quizes

#### Question #0
What is the ouput of this code?
```javascript
function myFunction(a) {
    console.log(a);
}

const a = 12;
myFunction(89);
```
* [ ] 2
* [ ] 1
* [ ] 12
* [X] 89

#### Question #1
What is the output of this code?
```javascript
let b = 1;

function myFunction(a) {
    console.log(a + b);
    b = a;
}

myFunction(3);
myFunction(4);
```
* [ ] 3, 7
* [ ] 3, 4
* [X] 4, 7
* [ ] 4, 3

#### Question #2
What is the output of this code?
```javascript
function myFunction(a) {
    console.log(a + b);
}

const b = 79;
myFunction(10);
```
* [X] 89
* [ ] 10
* [ ] 79


#### Question #3
What is the output of this code?
```javascript
const number = 12;
function myFunction(a) {
    console.log(a);
}

myFunction(number);
```
* [ ] 2
* [ ] 1
* [X] 12

#### Question #4
What is the output of this code?
```javascript
function myFunction(a) {
    console.log(a);
}

const number = 12;
myFunction(number);
```
* [ ] 2
* [ ] 1
* [X] 12

#### Question #5
What is the output of this code?
```javascript
function myFunction(a) {
    console.log(a);
}

myFunction(12);
```
* [ ] 2
* [ ] 1
* [X] 12

#### Question #6
What is the output of this code?
```javascript
const b = 79;
function myFunction(a) {
    console.log(a + b);
}

myFunction(10);
```
* [ ] 79
* [X] 89
* [ ] 10

#### Question #7
What is the output of the following code?
```javascript
const a = 12;

function myFunction(a) {
    console.log(a);
}

myFunction(89);
```
