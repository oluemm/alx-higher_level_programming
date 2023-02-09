#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

// extract url path from cmd line args
const url = argv[2];

request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  } else {
    const resp = JSON.parse(body);
    const movies = resp.results;
    let number = 0;
    movies.forEach(movie => movie.characters.forEach(charUrl => {
      if (charUrl.slice(-3, -1) === '18') {
        number++;
      }
    }));
    console.log(number);
  }
});
