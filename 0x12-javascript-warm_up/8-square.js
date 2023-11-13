#!/usr/bin/node
const num = parseInt(process.argv[2]);

if (!isNaN(num)) {
  let i = 0;
  while (i < num) {
    let j = 0;
    let square = '';
    while (j < num) {
      square += 'X';
      j++;
    }
    i++;
    console.log(square);
  }
} else { console.log('Missing size'); }
