#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const BaseUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieID = argv[2];
const url = BaseUrl + movieID;

function getNames(userurl) {
  request.get(userurl, function (err, resp, body) {
    if (err) {
      return console.error(err);
    }
    const fullname = JSON.parse(body).name;
    console.log(fullname);
  });
}
request.get(url, function (error, response, body) {
  if (error) {
    return console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    characters.forEach(character => {
      getNames(character);
    });
  }
});
