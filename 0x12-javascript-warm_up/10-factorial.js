#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * (factorial(n - 1));
  }
}
const args = parseInt(process.argv[2]);
const result = factorial(args);
console.log(result);
