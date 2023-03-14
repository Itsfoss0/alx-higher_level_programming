#!/usr/bin/node

/*
Ok, this is by far the worst algorithim I've written,
with a time Complexity of O(n)

Ill have to optimize this one :(:(:(
*/
exports.esrever = function (list) {
  const listLen = list.length;
  const newList = [];

  for (let i = listLen; i >= 0; i--) {
    newList.push(list[i]);
  }
  return (newList.slice(1, newList.length));
};
