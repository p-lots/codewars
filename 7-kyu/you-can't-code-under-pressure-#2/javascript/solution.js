function Counter() {
  this.check = function() {
    return this.count;
  }
  this.increment = function() {
    return this.count++;
  }
  this.count = 0;
};