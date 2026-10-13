// extend all numbers with toBits()
Number.prototype.toBits = function(minLength = 8) {
  return this.toString(2).padStart(minLength, "0");
}