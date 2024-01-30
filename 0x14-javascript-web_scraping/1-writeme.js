#!/usr/bin/node
// Writes a string to a file.

const fs = require('fs');
const file = process.argv[2];

fs.writeFile(file, process.argv[3], 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
});
