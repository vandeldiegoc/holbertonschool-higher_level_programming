#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const myArgs = process.argv.slice(2);
  myArgs.sort(function (a, b) {
    return b - a;
  });
  console.log(myArgs[1]);
}
