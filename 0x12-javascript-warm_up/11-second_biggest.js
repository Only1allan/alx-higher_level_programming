#!/usr/bin/node
const n = process.argv.slice(2);
console.log(n <= 3 ? '0' : search(n));

function search (n) {
  n.sort((a, b) => b - a);
  if (n.length >= 2) {
    return n[1];
  }
}
