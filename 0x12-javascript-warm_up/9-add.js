#!/usr/bin/node
function add (a, b) {
  const arg1 = parseInt(a);
  const arg2 = parseInt(b);

  if (isNaN(arg1) || isNaN(arg2)) {
    console.log('NaN');
  } else {
    console.log(arg1 + arg2);
  }
}
add(process.argv[2], process.argv[3]);
