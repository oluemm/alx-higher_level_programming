#!/usr/bin/node

const request = require('request');
const args = require('process');

// extract url path from cmd line args
const base = 'https://swapi-api.alx-tools.com/api/films/';
const id = args.argv[2];
const url = base + id;
// console.log(url);

request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  } else {
    const movie = JSON.parse(body);
    const movieTitle = movie.title;
    console.log(movieTitle);
  }
});
