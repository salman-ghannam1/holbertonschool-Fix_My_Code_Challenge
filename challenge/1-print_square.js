#!/usr/bin/node
/*
 * Print a square using the character #
 */

if (process.argv.length <= 2) {
  console.log('Missing size');
  process.exit(1);
}

const size = parseInt(process.argv[2]);

for (let i = 0; i < size; i++) {
  let row = '';

  for (let j = 0; j < size; j++) {
    row += '#';
  }

  console.log(row);
}
