#!/usr/bin/node

function maxValue (iterable) {
  let maxv = iterable[0];
  for (let i = 0; i <= iterable.length; i++) {
    if (iterable[i] > maxv) {
      maxv = iterable[i];
    }
  }
  return (maxv);
}

if (process.argv.length < 3) {
  console.log('0');
} else if (process.argv.length === 3) {
  console.log('1');
} else {
  const argsArray = process.argv.slice(2, parseInt(process.argv.length));
  const numsArray = argsArray.map(Number, argsArray);
  console.log(maxValue(numsArray));
}
