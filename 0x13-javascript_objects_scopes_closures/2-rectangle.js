#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    /* check if width and height vals are > than 0 */
    if (w > 0 && h > 0) {
      /* assign the given value to its respective variable */
      [this.width, this.height] = [w, h];
    }
  }
};
