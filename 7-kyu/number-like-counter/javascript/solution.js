function Counter() {
  this.num = 0;
}

Counter.prototype.incr = function() {
  this.num += 1;
}

Counter.prototype.valueOf = function() {
  return this.num;
}