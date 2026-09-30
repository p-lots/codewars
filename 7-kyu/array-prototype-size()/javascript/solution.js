Array.prototype.size = function() {
  let arrayLength = 0;
  this.forEach(_ => arrayLength++);
  return arrayLength;
};