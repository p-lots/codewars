Array.range = function(start, count) {
  return Array.from({ length: count }, (_, idx) => start + idx);
}

Array.prototype.sum = function() {
  return this.reduce((acc, nxt) => acc + nxt, 0);
}