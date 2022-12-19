#!/usr/bin/node

const { argv } = require('node:process');

const argsLength = argv.length;
if (argsLength === 2) {
  console.log('No argument');
} else if (argsLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
