#!/usr/bin/node

function factorial (number) {
  if (number === 1) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}

const value = process.argv[2];
if (isNaN(value)) {
  console.log('1');
} else {
  console.log(factorial(value));
}
