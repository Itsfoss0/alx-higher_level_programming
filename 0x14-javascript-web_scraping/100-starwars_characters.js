#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = baseUrl.concat(movieId);

request(fullUrl, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    // Create a variable to store the number of characters processed
    let charactersProcessed = 0;
    // Create an empty array to store the character names
    const characterNames = [];
    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error) {
          const charName = JSON.parse(body).name;
          // Add the character name to the array
          characterNames.push(charName);
        }
        // Increment the charactersProcessed variable
        charactersProcessed++;
        // Check if all characters have been processed
        if (charactersProcessed === characters.length) {
          // Log the character names when all characters have been processed
          characterNames.forEach((actor) => {
            console.log(actor);
          });
        }
      });
    });
  } else {
    console.log(error);
  }
});
