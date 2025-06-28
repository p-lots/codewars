// Recover toString() here :)

Number.prototype.toString = function() {
  return "" + this;
}

Boolean.prototype.toString = function() {
  return "" + this;
}

Array.prototype.toString = function() {
  let strng = "[";
  for (const elem of this) {
    strng += elem + ",";
  }
  if (strng.length > 1) {
    strng = strng.slice(0, -1);
  }
  return strng + "]";
}