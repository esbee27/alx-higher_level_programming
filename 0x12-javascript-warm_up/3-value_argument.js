#!/usr/bin/node
// Prinys the first argument passed

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
