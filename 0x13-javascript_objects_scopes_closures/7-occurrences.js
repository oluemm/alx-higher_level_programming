#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce(
    /* if current == searchElement increase count by 1 */
    (count, current) => current === searchElement ? count + 1 : count, 0
  );
};
