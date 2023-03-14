#!/usr/bin/node
const ParentSquare = require('./5-square');

module.exports = class Square extends ParentSquare {
  constructor (size) {
    super(size, size);
  }
};
