#!/usr/bin/node

const request = require('request');
const args = require('process');

// extract url path from cmd line args
const wedge = 'https://swapi-api.alx-tools.com/api/people/18/';
const url = args.argv[2];

request(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  } else {
    const resp = JSON.parse(body);
    const movies = resp.results;
    let number = 0;
    for (const i in movies) {
      const charlist = movies[i].characters;
      if (charlist.includes(wedge)) {
        number = number + 1;
      }
    }
    console.log(number);
  }
});
