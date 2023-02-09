#!/usr/bin/node
var arguments = process.argv;
// import file system module
var fs = require('fs');

file_path = arguments[2];
fs.readFile(file_path, function (err, data) {
	if (err) {
		return console.error(err);
	}
	console.log(data.toString());
});
