#!/usr/bin/node
console.log(process.argv.slice(2)[0] === undefined ? 'Not a number' : 'My number: ' + process.argv.slice(2)[0]);
