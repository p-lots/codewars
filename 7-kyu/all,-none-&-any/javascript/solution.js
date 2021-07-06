Array.prototype.all = function (p) {
  for (const elem of this) {
    if (!p(elem)) {
      return false;
    }
  }
  return true;
};

Array.prototype.none = function (p) {
  for (const elem of this) {
    if (p(elem)) {
      return false;
    }
  }
  return true;
};

Array.prototype.any = function (p) {
  for (const elem of this) {
    if (p(elem)) {
      return true;
    }
  }
  return false;
};