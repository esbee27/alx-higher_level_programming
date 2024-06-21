#!/usr/bin/node
// Prints a looo usingbthe number ofbthe first argument

const x = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
}
