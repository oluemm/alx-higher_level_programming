#!/usr/bin/node

const request = require('request');
const args = require('process');

// extract url path from cmd line args
const url = args.argv[2];
request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
