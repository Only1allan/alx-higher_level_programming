#!/usr/bin/node
// Prints all characters of a Star Wars movie:

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, response, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, function (err, response, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  } else {
    console.log(err);
  }
}
);
