#!/usr/bin/node
// get the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const url = process.argv[2];

request(url, function (err, response, body) {
    if (err) {
        return console.log(err);
    }
    fs.writeFile(process.argv[3], body, 'utf8', function (err) {
        if (err) {
            return console.log(err);
        }
    });
}
);
