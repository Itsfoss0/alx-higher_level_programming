#!/usr/bin/node

const parsedVal = parseInt(process.argv[2]);
if (!isNaN(parsedVal)) {
  console.log(`My number: ${parsedVal}`);
} else {
  console.log('Not a number');
}
