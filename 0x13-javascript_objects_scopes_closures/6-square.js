#!/usr/bin/node

/**
 * inherit from defined Square class
 */
module.exports = class Square extends require('./5-square.js') {
  /* character print function that prints a square using the given char */
  charPrint (c) {
    /* checks if no argument was passed */
    if (c === undefined) {
      this.print(); /* calls the default inherited print */
    } else {
      /* print the square using the given char */
      for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }
    }
  }
};
