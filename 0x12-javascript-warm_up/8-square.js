#!/usr/bin/node
if (isNaN(parseInt(process.argv[2], 10))) {
  console.log('Missing size');
} else {
  let x = 0;
  for (x = 0; x < process.argv[2]; x++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
