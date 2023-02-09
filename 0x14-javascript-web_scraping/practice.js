#!/usr/bin/node

var fs = require("fs");

var arguments = process.argv;
file = arguments[2];


// Asynchronous read
fs.readFile(file, function (err, data) {
	if (err) {
		return console.error(err);
	}
	console.log(data.toString());
});
