#!/usr/bin/node
exports.converter = function (base) {
  return function (dec) {
    return dec.toString(base);
  };
};
