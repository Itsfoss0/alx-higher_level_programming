#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      [this.width, this.height] = [w, h];
    }
  }

  print () {
    let sizeY = this.height;
    while (sizeY > 0) {
      console.log('X'.repeat(this.width));
      sizeY -= 1;
    }
  }
};
