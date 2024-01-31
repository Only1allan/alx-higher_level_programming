#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
    if (err) {
        return console.log(err);
    }
    let count = 0;
    const results = JSON.parse(body).results;
    for (const film of results) {
        for (const character of film.characters) {
        if (character.includes('18')) {
            count++;
        }
        }
    }
    console.log(count);
    });
