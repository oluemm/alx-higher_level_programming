#!/usr/bin/node

const fs = require('fs');

const args = require('process');
const file = args.argv[2];

// Asynchronous read
fs.readFile(file, function (err, data) {
  if (err) {
    // If an error occurred during the reading, print the error object
    return console.error(err);
  }
  console.log(data.toString());
});
