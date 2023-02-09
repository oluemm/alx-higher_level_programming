#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const { argv } = require('process');

const url = argv[2];
const filepath = argv[3];

request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  }
  const message = body;
  fs.writeFile(filepath, message, function (error) {
    if (error) {
      return console.error(error);
    }
  });
});
