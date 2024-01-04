#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, (error, response, body) => {
  if (error) console.log(error);
  fs.writeFileSync(fileName, body, { encoding: 'utf-8' });
});
