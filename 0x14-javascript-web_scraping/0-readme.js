#!/usr/bin/node

// import file system module
const fs = require('fs');

const args = require('process');
const file = args.argv[2];
fs.readFile(file, function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data.toString());
});
