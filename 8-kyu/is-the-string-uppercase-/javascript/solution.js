String.prototype.isUpperCase = function() {
  return this.split("").every((elem) => elem === elem.toUpperCase());
};
