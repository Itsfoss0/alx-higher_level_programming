#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (const elem of list) {
    if (elem === searchElement) {
      occurences += 1;
    }
  }
  return (occurences);
};
