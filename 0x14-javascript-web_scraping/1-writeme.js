#!/usr/bin/node

const fs = require('fs');

const fileName = process.argv[2];
const fileContent = process.argv[3];

fs.writeFile(fileName, fileContent, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
