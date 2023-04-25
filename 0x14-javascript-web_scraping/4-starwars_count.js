#!/usr/bin/node
const request = require('request');
const API_URL = process.argv[2];
let movieCount = 0;

request(API_URL, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const results = JSON.parse(body).results;
  for (const filmIdx in results) {
    const filmChars = results[filmIdx].characters;
    for (const charIndex in filmChars) {
      if (filmChars[charIndex].includes('18')) {
        movieCount += 1;
      }
    }
  }
  console.log(movieCount);
});
