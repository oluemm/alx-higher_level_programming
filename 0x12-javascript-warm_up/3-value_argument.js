#!/usr/bin/node

const { argv } = require('node:process');

const argsLength = argv.length;
if (argsLength === 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
