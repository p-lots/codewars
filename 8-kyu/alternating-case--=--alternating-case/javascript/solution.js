String.prototype.toAlternatingCase = function () {
  return this.split("").map((elem) => elem.toLowerCase() === elem ? elem.toUpperCase() : elem.toLowerCase()).join("");
};
