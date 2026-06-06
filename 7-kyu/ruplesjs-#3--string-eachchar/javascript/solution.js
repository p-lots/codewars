String.prototype.eachChar = function(arg) {
  if (typeof arg === "string") {
    return this.split("").reduce((accum, nxt) => {
      accum += nxt + arg;
      return accum;
    }, "");
  }
  return this.split("").map(arg).join("");
};