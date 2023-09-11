#!/usr/bin/node
const arg = process.argv.slice(2)[0];
if (arg === 'undefined' || isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    let row = '';
    for (let j = 0; j < arg; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
