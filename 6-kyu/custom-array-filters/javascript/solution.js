Array.prototype.even = function() {
  return this.filter((n) => Number.isInteger(n)).filter((n) => n % 2 === 0);
}

Array.prototype.odd = function() {
  return this.filter((n) => Number.isInteger(n)).filter((n) => n % 2 === 1);
}

Array.prototype.under = function(x) {
  return this.filter((n) => Number.isInteger(n)).filter((n) => n < x);
}

Array.prototype.over = function(x) {
  return this.filter((n) => Number.isInteger(n)).filter((n) => n > x);
}

Array.prototype.inRange = function(min, max) {
  return this.filter((n) => Number.isInteger(n)).filter((n) => n >= min && n <= max);
}
