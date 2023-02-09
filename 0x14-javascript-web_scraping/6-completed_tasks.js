#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const returnDict = {};
  const todos = JSON.parse(body);
  todos.forEach(todo => {
    if (todo.completed) {
      const userID = todo.userId;
      // if userID aleady exists in the dictionary
      if (returnDict[userID] !== undefined) {
        returnDict[userID]++; // count occurence
      } else {
        // create it as 1st occurence
        returnDict[userID] = 1;
      }
    }
  });
  console.log(returnDict);
});
