#!/usr/bin/node

exports.esrever = function (list) {
  const len = (list.length) - 1;
  const listnew = [];
  for (let i = len; i >= 0; i--) {
    listnew.push(list[i]);
  }
  return (listnew);
};
