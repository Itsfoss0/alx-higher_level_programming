#!/usr/bin/node

exports.callMeMoby = function (x, theFunction){
  while (x) {
    theFunction();
    x += 1;
  }
}
