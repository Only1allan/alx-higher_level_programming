#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (myArr, item) {
    myArr.push(item);
    return myArr;
  }, []);
};
