#!/usr/bin/node
function factorial (n) {
return n === 0 || isNaN(n) ? 1 : n *factorial(n - 1);
}
const args = parseInt(process.argv[2]);
const result = factorial(args);
console.log(result);
