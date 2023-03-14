#!/usr/bin/node
const ParentSquare = require('./5-square');

module.exports = class Square extends ParentSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.size; i++) {
        console.log(String(c).repeat(this.size));
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log('X'.repeat(this.size));
      }
    }
  }
};
