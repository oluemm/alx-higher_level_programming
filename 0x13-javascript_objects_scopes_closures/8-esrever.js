#!/usr/bin/node
/* a function that appends an element to an array and returns the array */
const rev = function (array, current) {
  array.push(current);
  return array;
};
exports.esrever = function (list) {
  /* reduceRight takes a callback func and array to use */
  return list.reduceRight(rev, []);
};
