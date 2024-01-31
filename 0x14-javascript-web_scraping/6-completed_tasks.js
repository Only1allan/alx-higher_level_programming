#!/usr/bin/node
// Computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  const results = JSON.parse(body);
  const completed = {};
  for (const task of results) {
    if (task.completed === true) {
      if (completed[task.userId] === undefined) {
        completed[task.userId] = 1;
      } else {
        completed[task.userId] += 1;
      }
    }
  }
  console.log(completed);
}
);
