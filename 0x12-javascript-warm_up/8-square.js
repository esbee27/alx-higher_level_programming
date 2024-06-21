#!/usr/bin/node
// Prints a square

const x = parseInt(process.argv[2]);
if (isNaN(process.argv[2]) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
