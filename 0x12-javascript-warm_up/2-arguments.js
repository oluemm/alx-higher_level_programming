#!/usr/bin/node

const { argv } = require('node:process');

const argsLength = argv.length;
console.log(argsLength === 2 ? 'No argument' : argsLength === 3 ? 'Argument found' : 'Arguments found');
