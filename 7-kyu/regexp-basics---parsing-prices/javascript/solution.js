String.prototype.toCents = function() {
  const format = /^\$(\d+\.\d{2})$/;
  const matches = format.exec(this);
  if (matches === null) {
    return null;
  }
  const rawValue = matches[1].replace(".", "");
  return Number(rawValue);
}