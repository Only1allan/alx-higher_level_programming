#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/:id' + process.argv[2];

request(url, function (error, response, body) {
  if (error) console.log(error);
  console.log(JSON.parse(body).title);
});
