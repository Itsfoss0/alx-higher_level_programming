#!/usr/bin/node

const origList = require('./100-data').list;

const newList = origList.map((elem, idx) => elem * idx);

console.log(origList);
console.log(newList);
