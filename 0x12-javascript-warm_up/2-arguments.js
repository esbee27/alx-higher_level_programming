#!/usr/bin/node
// A script tht orints a  message depending in the number of argumwnts passed

if (process.argv.length < 3) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
