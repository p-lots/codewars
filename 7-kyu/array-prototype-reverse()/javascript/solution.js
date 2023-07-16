Array.prototype.reverse = function() {
  if (this.length === 0) {
    return this;
  }
  for (let i = 0; i < this.length / 2; i++) {
    const temp = this[i];
    this[i] = this[this.length - i - 1];
    this[this.length - i - 1] = temp;
  }
  return this;
};
