#!/usr/bin/node
exports.converter = function (base) {
  /* toString(base) converts a given str to number in given 'base' */
  return num => num.toString(base);
};
