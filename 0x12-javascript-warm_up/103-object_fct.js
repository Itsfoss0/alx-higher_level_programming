#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr () {
    this.value += 1;
  }
};
console.log(myObject);
/*
  YOUR CODE HERE
  */
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
