#!/usr/bin/node
console.log(process.argv.slice(2)[0] === undefined ? 'No argument' : process.argv.slice(2)[0]);
