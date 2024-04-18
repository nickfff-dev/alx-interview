#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Please provide a movie ID as a command-line argument.');
  process.exit(1);
}

const reqCharacters = url => {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (err, res, body) => {
      if (err) {
        reject(err);
      }
      resolve(body);
    });
  });
};

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, { json: true }, async (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  for (const character of body.characters) {
    const response = await reqCharacters(character);
    console.log(response.name);
  }
});
