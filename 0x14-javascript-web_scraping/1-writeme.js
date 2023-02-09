#!/usr/bin/node

// import file system module
const fs = require('fs');
const args = require('process');

// extract file path from cmd line args
const file = args.argv[2];
// extract file path from cmd line args
const string = args.argv[3];

fs.writeFile(file, string, function (err) {
  if (err) {
    // If an error occurred during the reading, print the error object
    return console.error(err);
  }
});
