#!/usr/bin/node
// Prints the title of a
// Star Wars movie where the episode number matches a given integer.

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + process.argv[2], function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
